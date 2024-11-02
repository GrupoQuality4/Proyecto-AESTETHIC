import sqlite3

# Ruta a la base de datos
db_path = 'C:\\Users\\Flia Caro Sosa Veron\\OneDrive\\Desktop\\Proyecto-AESTETHIC\\instance\\Aestethic.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Paso 1: Crear el rol de administrador si no existe
admin_role_name = "Administrador"
permissions = "manage_roles,assign_roles,create_service_category,manage_service_category"  # Permisos del rol

# Verificar si el rol ya existe
cursor.execute("SELECT id FROM role WHERE name = ?", (admin_role_name,))
role = cursor.fetchone()

if role:
    role_id = role[0]
    print(f"Rol '{admin_role_name}' ya existe con id {role_id}.")
else:
    # Crear el rol de administrador
    cursor.execute("INSERT INTO role (name, permissions) VALUES (?, ?)", (admin_role_name, permissions))
    conn.commit()
    role_id = cursor.lastrowid
    print(f"Rol '{admin_role_name}' creado con id {role_id}.")

# Paso 2: Asignar el rol de administrador al usuario
user_email = "aestheticestetica22@gmail.com"

# Obtener el id del usuario
cursor.execute("SELECT id FROM user WHERE email = ?", (user_email,))
user = cursor.fetchone()

if user:
    user_id = user[0]
    # Insertar en roles_users para asignar el rol al usuario
    cursor.execute("INSERT INTO roles_users (user_id, role_id) VALUES (?, ?)", (user_id, role_id))
    conn.commit()
    print(f"Rol '{admin_role_name}' asignado al usuario con email '{user_email}'.")
else:
    print(f"No se encontró un usuario con el email '{user_email}'.")

# Cerrar la conexión a la base de datos
conn.close()

