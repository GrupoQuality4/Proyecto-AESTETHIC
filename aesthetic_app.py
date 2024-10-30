from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import g, render_template, request, redirect, url_for, flash, session, jsonify
from flask_migrate import Migrate
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import random
import os
import re
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
import validators
from models import db, User, Role, Servicio, VerificationToken, Reserva

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Aestethic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'aestheticestetica22@gmail.com'
app.config['MAIL_PASSWORD'] = 'hnwm mlzy lcah sgko'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

@app.before_request
def add_user_to_template():
    g.user_name = session.get('user_name', None)
    g.user_apellido = session.get('user_apellido', None)
    g.user_email = session.get('user_email', None)
    g.avatar_color = session.get('avatar_color', None)
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if user:
            session['user_roles'] = [role.name for role in user.roles]


def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_USERNAME']
    )
    mail.send(msg)

def generate_confirmation_token(email):
    return ts.dumps(email, salt='email-confirm-key')

def confirm_token(token, expiration=3600):
    try:
        email = ts.loads(token, salt='email-confirm-key', max_age=expiration)
    except:
        return False
    return email

@app.route('/')
def home():
    user_name = session.get('user_name', None)
    user_apellido = session.get('user_apellido', None)
    user_email = session.get('user_email', None)
    avatar_color = session.get('avatar_color', None)
    return render_template('Pag_Principal_AESTETIC.html', user_name=user_name, user_apellido=user_apellido, user_email=user_email, avatar_color=avatar_color)

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje_login = None

    if request.method == 'POST':
        email = request.form['usuario']
        password = request.form['contrasena']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            verification_token = VerificationToken.query.filter_by(user_id=user.id).first()

            if verification_token and verification_token.expires_at < datetime.utcnow():
                db.session.delete(verification_token)
                db.session.delete(user)
                db.session.commit()
                flash('La cuenta no fue verificada y ha sido eliminada. Regístrate de nuevo.', 'danger')
                return redirect(url_for('register'))

            session['user_id'] = user.id
            session['user_name'] = user.nombre
            session['user_apellido'] = user.apellido
            session['user_email'] = user.email
            session['avatar_color'] = generate_random_color()
            flash('Inicio de sesión exitoso', 'success')
            next_url = request.args.get('next')
            return redirect(next_url or url_for('home'))

        flash('Correo o contraseña incorrectos', 'danger')
    if request.args.get('next') == '/reservas':
        mensaje_login = "Inicia sesión para continuar con la reserva. Si no tienes una cuenta, regístrate."

    return render_template('Login.html', mensaje_login=mensaje_login)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_apellido', None)
    session.pop('user_email', None)
    session.pop('avatar_color', None)
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            password = data.get('contrasena')

            if not nombre.isalpha() or not apellido.isalpha():
                return jsonify(success=False, message='El nombre y apellido deben contener solo letras.')

            if not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                return jsonify(success=False, message='El correo debe ser una cuenta de Gmail.')

            if User.query.filter_by(email=email).first():
                return jsonify(success=False, message='El correo ya está registrado.')

            password_regex = r'^[A-Z][A-Za-z\d@$!%*#?&]{7,11}$'
            if not re.match(password_regex, password):
                return jsonify(success=False, message='La contraseña debe iniciar con una mayúscula, tener entre 8 y 12 caracteres, incluir al menos un número y un carácter especial.')

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(nombre=nombre, apellido=apellido, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            token = generate_confirmation_token(new_user.email)
            expires_at = datetime.utcnow() + timedelta(hours=24)
            verification_token = VerificationToken(token=token, user_id=new_user.id, expires_at=expires_at)
            db.session.add(verification_token)
            db.session.commit()

            confirm_url = url_for('confirm_email', token=token, _external=True)
            html = render_template('activate.html', confirm_url=confirm_url)
            subject = "Por favor confirma tu correo"
            send_email(new_user.email, subject, html)

            return jsonify(success=True)
        else:
            return jsonify(success=False, message="Tipo de contenido no soportado"), 415
    return render_template('Registro.html')


@app.route('/register_success')
def register_success():
    return render_template('register_success.html')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    verification_token = VerificationToken.query.filter_by(token=token).first_or_404()

    if verification_token.expires_at < datetime.utcnow():
        user = verification_token.user
        db.session.delete(verification_token)
        db.session.delete(user)
        db.session.commit()

        flash('El enlace de confirmación ha expirado. Por favor, regístrate de nuevo.', 'danger')
        return redirect(url_for('register'))
    
    user = verification_token.user
    db.session.delete(verification_token)
    db.session.commit()

    flash('Has confirmado tu correo electrónico. Gracias! Ahora puedes iniciar sesión.', 'success')
    return redirect(url_for('login'))

@app.route('/manage_roles', methods=['GET', 'POST'])
def manage_roles():
    if 'Administrador' not in session.get('user_roles', []):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('manage_roles.html')

@app.route('/assign_role', methods=['GET', 'POST'])
def assign_role():
    if 'Administrador' not in session.get('user_roles', []):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('assign_role.html')

@app.route('/create_service_category', methods=['GET', 'POST'])
def create_service_category():
    if 'Administrador' not in session.get('user_roles', []):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('create_service_category.html')

@app.route('/manage_service_category')
def manage_service_category():
    if 'Administrador' not in session.get('user_roles', []):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('manage_service_category.html')

def user_has_permission(user, permission):
    for role in user.roles:
        if permission in role.permissions.split(','):
            return True
    return False

@app.route('/restricted_page')
def restricted_page():
    user = User.query.get(session['user_id'])
    if not user_has_permission(user, 'access_restricted_page'):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('restricted_page.html')

@app.route('/buscar_servicios', methods=['GET'])
def buscar_servicios():
    query = request.args.get('query', '').lower()
    servicios = [
        {'nombre': 'Tratamientos Faciales', 'ruta': url_for('tratamiento_facial')},
        {'nombre': 'Depilación', 'ruta': url_for('tratamiento_depilacion')},
        {'nombre': 'Masajes', 'ruta': url_for('tratamiento_masajes')},
        {'nombre': 'Spa de Manos', 'ruta': url_for('tratamiento_spa_de_manos')},
        {'nombre': 'Tratamientos Corporales', 'ruta': url_for('tratamientos_corporales')}
    ]
    resultados = [s for s in servicios if query in s['nombre'].lower()]
    return jsonify(resultados)

@app.route('/servicios')
def servicios():
    return render_template('Servicios.html')

@app.route('/tratamientos_corporales')
def tratamientos_corporales():
    return render_template('service/Pag_Tratamiento Corporales.html')

@app.route('/tratamientos_facial')
def tratamiento_facial():
    return render_template('service/Pag_TratamientoFacial.html')

@app.route('/tratamientos_depilacion')
def tratamiento_depilacion():
    return render_template('service/Pag_Depilacion.html')

@app.route('/tratamientos_spa_de_manos')
def tratamiento_spa_de_manos():
    return render_template('service/Pag_SpaDeManos.html')

@app.route('/tratamientos_masajes')
def tratamiento_masajes():
    return render_template('service/Pag_Masajes.html')

@app.route('/novedades')
def novedades():
    return render_template('Novedades.html')

@app.route('/gif_card')
def gif_card():
    return render_template('Gif_Card.html')

@app.route('/contactos')
def contactos():
    return render_template('Contactos.html')

@app.route('/reservas')
def reservas():
    tratamiento = request.args.get('tratamiento', '')
    subservicio = request.args.get('subservicio', '')
    if 'user_id' not in session:
        return redirect(url_for('login', next='/reservas'))
    return render_template('Reservaciones.html', tratamiento=tratamiento, subservicio=subservicio)

@app.route('/historial_reservas')
def historial_reservas():
    if 'user_id' not in session:
        return redirect(url_for('login', next=url_for('historial_reservas')))
    
    user_id = session['user_id']
    reservas = Reserva.query.filter_by(user_id=user_id).order_by(Reserva.fecha_reserva.desc()).all()
    
    return render_template('historial_reservas.html', reservas=reservas)

@app.route('/servicio/<int:servicio_id>/reservar')
def reservar_servicio(servicio_id):
    if 'user_id' not in session:
        flash("Debes iniciar sesión para hacer una reserva.", "warning")
        return redirect(url_for('login', next=url_for('reservas')))
    return redirect(url_for('reservas'))

@app.route('/buscar_servicios_fecha', methods=['GET'])
def buscar_servicios_fecha():
    fecha = request.args.get('fecha')
    
    if not fecha:
        return jsonify({"error": "Fecha no proporcionada"}), 400
    servicios_disponibles = Servicio.query.filter_by(fecha_disponible=fecha).all()

    servicios = [{
        "titulo": servicio.titulo,
        "descripcion": servicio.descripcion,
        "precio": servicio.precio
    } for servicio in servicios_disponibles]
    
    return jsonify({"servicios": servicios})

@app.route('/carrito')
def carrito():
    user_name = session.get('user_name', None)
    user_apellido = session.get('user_apellido', None)
    user_email = session.get('user_email', None)
    avatar_color = session.get('avatar_color', None)
    return render_template('Carrito.html', user_name=user_name, user_apellido=user_apellido, user_email=user_email, avatar_color=avatar_color)

if __name__ == '__main__':
    app.run(debug=True)














