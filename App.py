import streamlit as st
import pandas as pd
import sqlite3
import base64
from utils.filtros import aplicar_filtros
from utils.mapa import construir_mapa
from streamlit_folium import st_folium

# ─── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title="Mapa del Delito - REGPOL PUNO",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Inyectar CSS ──────────────────────────────────────────────────────────────
with open("css/style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ─── Función para convertir GIF a base64 ──────────────────────────────────────
def get_base64_gif(path):
    with open(path, "rb") as g:
        return base64.b64encode(g.read()).decode()

# ─── Cargar datos desde SQLite (cacheado) ────────────────────────────────────
@st.cache_data
def cargar_datos():
    conn = sqlite3.connect("data/heatmap.db")
    df = pd.read_sql_query("SELECT * FROM denuncias", conn)
    conn.close()
    return df.dropna(subset=["Latitud", "Longitud"])

df = cargar_datos()

# ─── Panel flotante: filtros, KPI y texto ─────────────────────────────────────
# Usamos la barra lateral de Streamlit y la estilizamos como flotante pequeña
with st.sidebar:
    st.markdown("<h3 class='titulo-filtro'>🎯 FILTRAR BÚSQUEDA</h3>", unsafe_allow_html=True)
    # Aplicar filtros
    fecha, delito, unidad, filtro = aplicar_filtros(df)
    # KPI
    st.markdown(
    f"""
    <div class="kpi">
      Total de Denuncias:<br>
      <span class="kpi-num">{len(filtro)}</span>
    </div>
    """,
    unsafe_allow_html=True
    )

    # Texto adicional (GIF y pie)
    gif = get_base64_gif("assets/POLITA-GIF-DEMO-prueba.gif")
    st.image(f"data:image/gif;base64,{gif}", width=148)
    st.markdown("<p class='gif-text'>*UNTIC PNP PUNO*</p>", unsafe_allow_html=True)
    #st.markdown("<p class='gif-text'>*Todo los derechos reservados*</p>", unsafe_allow_html=True)
    #st.markdown("<p class='gif-text'>*2025*</p>", unsafe_allow_html=True)
# ─── Mostrar mapa folium ──────────────────────────────────────────────────────
mapa = construir_mapa(filtro)
st_folium(mapa, use_container_width=True, height=690) 