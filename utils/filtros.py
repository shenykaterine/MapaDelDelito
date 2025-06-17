import streamlit as st

def aplicar_filtros(df):
    fechas = df["Fecha"].astype(str).unique()
    delitos = df["Delito"].unique()
    unidades = df["Unidad PNP"].unique()

    fecha = st.selectbox("📅 Fecha", ["Todos"] + sorted(fechas.tolist()))
    delito = st.selectbox("🚨 Tipo de Delito", ["Todos"] + sorted(delitos.tolist()))
    unidad = st.selectbox("👮 Unidad PNP", ["Todas"] + sorted(unidades.tolist()))

    filtro = df.copy()
    if fecha != "Todos":
        filtro = filtro[filtro["Fecha"].astype(str) == fecha]
    if delito != "Todos":
        filtro = filtro[filtro["Delito"] == delito]
    if unidad != "Todas":
        filtro = filtro[filtro["Unidad PNP"] == unidad]

    return fecha, delito, unidad, filtro
