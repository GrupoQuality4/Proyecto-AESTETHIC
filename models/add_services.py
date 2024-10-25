import sqlite3

connection = sqlite3.connect('instance/Aestethic.db')
cursor = connection.cursor()


insert_query = """
INSERT INTO servicio (titulo, categoria, descripcion, precio)
VALUES (?, ?, ?, ?)
"""


massage_services = [
    ('Masaje Relajante con Aromaterapia', 'Masajes', 'Un masaje corporal completo utilizando aceites esenciales aromáticos para relajar el cuerpo y la mente. Ideal para aliviar el estrés y mejorar el bienestar general.', 79.99),
    ('Masaje Descontracturante', 'Masajes', 'Masaje enfocado en liberar la tensión muscular acumulada en áreas específicas, como la espalda, el cuello y los hombros. Utiliza presión firme para aliviar nudos y mejorar la flexibilidad muscular.', 129.99),
    ('Masaje con Piedras Calientes', 'Masajes', 'Masaje terapéutico que combina movimientos suaves con la aplicación de piedras volcánicas calientes para relajar profundamente los músculos, mejorar la circulación y reducir el estrés.', 199.99),
    ('Masaje de Reflexología', 'Masajes', 'Masaje especializado en los pies o manos que estimula puntos de presión específicos, basados en la medicina tradicional china, para mejorar el equilibrio y la salud de todo el cuerpo.', 49.99)
]


for service in massage_services:
    cursor.execute(insert_query, service)


connection.commit()

cursor.close()
connection.close()

print("Servicios de Masajes agregados con éxito.")







