import sqlite3

# Ruta a tu archivo de base de datos SQLite
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Añadir la columna 'is_used' a la tabla 'verification_tokens'
try:
    cursor.execute("ALTER TABLE verification_tokens ADD COLUMN is_used BOOLEAN DEFAULT 0;")
    print("Columna 'is_used' añadida correctamente.")
except sqlite3.OperationalError as e:
    print("Error:", e)
    print("La columna 'is_used' ya podría existir o ocurrió otro problema.")

# Guarda los cambios y cierra la conexión
conn.commit()
conn.close()
