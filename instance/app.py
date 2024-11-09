import sqlite3

# Ruta de la base de datos
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conexión a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# IDs de los tokens que quieres marcar como usados
tokens_a_marcar = [1, 4]

# Construye y ejecuta la consulta de actualización
try:
    cursor.executemany("UPDATE verification_tokens SET is_used = 1 WHERE id = ?", [(id,) for id in tokens_a_marcar])
    conn.commit()
    print("Tokens actualizados correctamente.")
except Exception as e:
    conn.rollback()
    print(f"Error al actualizar tokens: {e}")
finally:
    # Cierra la conexión
    conn.close()

