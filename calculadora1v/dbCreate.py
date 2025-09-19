import sqlite3

# Crear la base de datos (se genera el archivo tareas.db)
conn = sqlite3.connect("tareas.db")
cursor = conn.cursor()

# Crear la tabla tareas
cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    estado TEXT DEFAULT 'Pendiente'
)
""")

conn.commit()
conn.close()

print("✅ Base de datos y tabla 'tareas' creadas con éxito.")
