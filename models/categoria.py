from . import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    servicios = db.relationship('Servicio', back_populates='categoria')

    def __repr__(self):
        return f"<Categoria {self.nombre}>"
