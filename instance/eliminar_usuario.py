import sqlite3

db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def renombrar_tabla(old_name, new_name):
    rename_query = f"ALTER TABLE {old_name} RENAME TO {new_name};"
    cursor.execute(rename_query)
    conn.commit()
    print(f"Tabla '{old_name}' renombrada a '{new_name}'.")

renombrar_tabla('user', 'users')
conn.close()
