import sqlite3

# Ruta a tu base de datos
db_path = 'C:\\Users\\Tecno\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conexión a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Renombrar la tabla de 'servicio' a 'servicios'
cursor.execute('''
    ALTER TABLE servicio RENAME TO servicios
''')

print("Tabla renombrada correctamente.")
conn.commit()
conn.close()
