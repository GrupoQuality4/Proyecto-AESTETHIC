
import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "Aestethic.db"

if not db_path.is_file():
    print("Error: No se encontró la base de datos.")
    raise SystemExit

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Mostrar usuarios registrados
cursor.execute("SELECT user_id, nombre, apellido, email FROM users")

print("USUARIOS REGISTRADOS:")
for usuario in cursor.fetchall():
    print(usuario)

# Seleccionar usuarios
ids_a_eliminar = input(
    "\nIngrese los IDs a eliminar, separados por comas: "
)

try:
    ids_a_eliminar = [
        int(id.strip())
        for id in ids_a_eliminar.split(",")
    ]

    placeholders = ", ".join("?" for _ in ids_a_eliminar)

    confirmacion = input(
        f"¿Eliminar estos usuarios {ids_a_eliminar}? Escriba SI: "
    )

    if confirmacion == "SI":
        query = f"DELETE FROM users WHERE user_id IN ({placeholders})"
        cursor.execute(query, ids_a_eliminar)
        cantidad = cursor.rowcount
        conn.commit()

        print(f"Se eliminaron {cantidad} usuarios.")
    else:
        print("Operación cancelada.")

except (sqlite3.Error, ValueError) as e:
    conn.rollback()
    print(f"Error al eliminar usuarios: {e}")

finally:
    conn.close()
