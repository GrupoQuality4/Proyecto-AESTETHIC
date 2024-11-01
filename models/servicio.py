from . import db

class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String, nullable=False)
    titulo = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=True)
    precio = db.Column(db.Float, nullable=False)

    horarios = db.relationship('Horario', backref='servicio', lazy=True)


