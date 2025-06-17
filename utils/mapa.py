import folium
from folium.plugins import HeatMap, MarkerCluster

def construir_mapa(filtro):
    # 📌 Crear el mapa base centrado en Puno
    m = folium.Map(location=[-15.84, -70.02], zoom_start=7, tiles="CartoDB positron")

    # 📌 Prepara los datos válidos para capas
    heat_data = filtro[["Latitud", "Longitud"]].dropna().values.tolist()

    # 📌 Capa de calor (solo si hay datos)
    if heat_data:
        HeatMap(
            heat_data,
            radius=12,
            blur=15,
            max_zoom=10,
            gradient={
                0.2: 'blue',
                0.4: 'lime',
                0.6: 'orange',
                0.8: 'red',
                1.0: 'darkred'
            }
        ).add_to(m)

    # 📌 Mostrar máximo 300 marcadores individuales o usar cluster
    total_puntos = len(filtro)

    if total_puntos <= 300:
        # Marcadores individuales
        for _, row in filtro.iterrows():
            try:
                folium.Marker(
                    location=[row["Latitud"], row["Longitud"]],
                    popup=folium.Popup(f"""
                        <b>Fecha:</b> {row.get('Fecha', 'N/A')}<br>
                        <b>Delito:</b> {row.get('Delito', 'N/A')}<br>
                        <b>Unidad:</b> {row.get('Unidad PNP', 'N/A')}<br>
                        <b>Distrito:</b> {row.get('Distrito', 'N/A')}
                    """, max_width=250),
                    icon=folium.Icon(color="red", icon="info-sign")
                ).add_to(m)
            except:
                continue  # Evita errores si falta alguna coordenada
    else:
        # Agrupamiento dinámico con cluster
        cluster = MarkerCluster().add_to(m)
        for _, row in filtro.iterrows():
            try:
                folium.Marker(
                    location=[row["Latitud"], row["Longitud"]],
                    popup=folium.Popup(f"""
                        <b>Fecha:</b> {row.get('Fecha', 'N/A')}<br>
                        <b>Delito:</b> {row.get('Delito', 'N/A')}<br>
                        <b>Unidad:</b> {row.get('Unidad PNP', 'N/A')}<br>
                        <b>Distrito:</b> {row.get('Distrito', 'N/A')}
                    """, max_width=250),
                    icon=folium.Icon(color="red", icon="info-sign")
                ).add_to(cluster)
            except:
                continue

    # 📌 Capas adicionales
    folium.TileLayer(
    tiles="https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg",
    name="Stamen Terrain",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors"
    ).add_to(m)

    folium.TileLayer(
    tiles="https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png",
    name="Stamen Toner",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors"
    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m
