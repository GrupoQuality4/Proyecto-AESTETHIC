from . import db

class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String)
    precio = db.Column(db.Float, nullable=False)
    categorias = db.Column(db.Integer, db.ForeignKey('categorias.id'))  # Definir como clave foránea

    # Relación con el modelo Categoria
    categoria = db.relationship('Categoria', back_populates='servicios')
    
    # Relación con el modelo Horario
    horarios = db.relationship('Horario', back_populates='servicio')

    def __repr__(self):
        return f"<Servicio {self.titulo}>"




