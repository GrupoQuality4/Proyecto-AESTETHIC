import sqlite3

# Ruta a tu archivo de base de datos SQLite
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Cambiar el nombre de la tabla `verification_token` a `verification_tokens`
    cursor.execute('''
        ALTER TABLE verification_token RENAME TO verification_tokens;
    ''')
    conn.commit()
    print("Tabla renombrada exitosamente a 'verification_tokens'.")

except sqlite3.OperationalError as e:
    print(f"Error al renombrar la tabla: {e}")

# Cerrar la conexión
conn.close()
