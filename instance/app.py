
import sqlite3
from pathlib import Path

# Ruta automática a la base de datos
db_path = Path(__file__).resolve().parent / "Aestethic.db"

if not db_path.is_file():
    print("Error: No se encontró la base de datos.")
    raise SystemExit

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Contar las reservas existentes
    cursor.execute("SELECT COUNT(*) FROM reservas")
    total = cursor.fetchone()[0]

    print(f"Reservas registradas: {total}")

    if total > 0:
        confirmacion = input(
            "¿Desea eliminar TODAS las reservas? Escriba SI: "
        )

        if confirmacion.upper() == "SI":
            cursor.execute("DELETE FROM reservas")
            eliminadas = cursor.rowcount
            conn.commit()

            print(f"Se eliminaron {eliminadas} reservas correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No hay reservas para eliminar.")

except sqlite3.Error as error:
    conn.rollback()
    print(f"Error al eliminar reservas: {error}")

finally:
    cursor.close()
    conn.close()
    print("Conexión cerrada.")

