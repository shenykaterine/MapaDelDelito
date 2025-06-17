import pandas as pd
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect("data/heatmap.db")
cursor = conn.cursor()

# Obtener las tablas de la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

print("🔍 Tablas encontradas en la base de datos:")
for tabla in tablas:
    print("-", tabla[0])

conn.close()