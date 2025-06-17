import pandas as pd
import sqlite3

# Ruta del archivo Excel
archivo_excel = "data/heatmap.xlsx"

# Leer la hoja principal
df = pd.read_excel(archivo_excel)

# Quitar filas sin latitud o longitud
df = df.dropna(subset=["Latitud", "Longitud"])

# Ruta de la base de datos SQLite
archivo_db = "data/heatmap.db"

# Crear conexión y guardar en SQLite
conn = sqlite3.connect(archivo_db)
df.to_sql("denuncias", conn, if_exists="replace", index=False)
conn.close()

print("✅ Base de datos SQLite creada correctamente en 'data/heatmap.db'")
