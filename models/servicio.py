from . import db

class Servicio(db.Model):
    __tablename__ = 'servicio'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    horarios = db.relationship('Horarios', backref='servicio', lazy=True)

