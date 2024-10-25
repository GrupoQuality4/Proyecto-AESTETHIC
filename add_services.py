from aesthetic_app import db
from models.servicio import Servicio

# Crear instancias de servicios
servicios = [
    Servicio(titulo='Exfoliación Corporal', categoria='Tratamientos Corporales', descripcion='Un tratamiento que elimina las células muertas de la piel mejora su textura y luminosidad.', precio=79.99),
    Servicio(titulo='Envoltura de algas o barro', categoria='Tratamientos Corporales', descripcion='Ayuda a desintoxicar el cuerpo y a mejorar la circulación.', precio=129.99),
    Servicio(titulo='Masaje reafirmante', categoria='Tratamientos Corporales', descripcion='Ayuda a tonificar la piel y mejorar la elasticidad, ideal para combatir la flacidez.', precio=199.99),
    Servicio(titulo='Tratamiento de drenaje linfático', categoria='Tratamientos Corporales', descripcion='Un masaje suave que estimula el sistema linfático, eliminando toxinas y reduciendo la retención de líquidos.', precio=49.99)
]

# Agregar servicios a la base de datos
for servicio in servicios:
    db.session.add(servicio)

# Confirmar cambios en la base de datos
db.session.commit()

print("Servicios agregados exitosamente.")

