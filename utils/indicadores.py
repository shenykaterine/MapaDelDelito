import streamlit as st

def mostrar_kpis(df, filtro):
    st.markdown(f"<div class='kpi'>📌 Total de Denuncias: <b>{len(df)}</b></div>",unsafe_allow_html=True)
    #st.markdown(f"<div class='kpi'>🕒 Rango de Fechas: <b>{df['Fecha'].min()} - {df['Fecha'].max()}</b></div>", unsafe_allow_html=True)
    #st.markdown(f"<div class='kpi'>🏘️ Unidades PNP: <b>{df['Unidad PNP'].nunique()}</b></div>", unsafe_allow_html=True)
    #st.markdown(f"<div class='kpi'>🚨 Delitos únicos: <b>{df['Delito'].nunique()}</b></div>", unsafe_allow_html=True)

