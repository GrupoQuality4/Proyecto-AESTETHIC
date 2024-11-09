from flask import Flask, g, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import random, os, re
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
import validators
from models import db, User, Role, Servicio, VerificationToken, Reserva, Horario, Categoria, Dia, BloqueHora

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
    try:
        msg = Message(subject, recipients=[to], html=template, sender=app.config['MAIL_USERNAME'])
        mail.send(msg)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_apellido', None)
    session.pop('user_email', None)
    session.pop('avatar_color', None)
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje_login = None

    # Verificar si hay un mensaje de registro exitoso en la sesión
    registro_exitoso = session.pop('registro_exitoso', None)

    if request.method == 'POST':
        email = request.form['usuario']
        password = request.form['contrasena']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            verification_token = VerificationToken.query.filter_by(user_id=user.user_id).first()
            if verification_token and verification_token.expires_at < datetime.utcnow():
                db.session.delete(verification_token)
                db.session.delete(user)
                db.session.commit()
                flash('La cuenta no fue verificada y ha sido eliminada. Regístrate de nuevo.', 'danger')
                return redirect(url_for('register'))

            # Guardar el user_id y otros detalles en la sesión
            session['user_id'] = user.user_id
            session['user_name'] = user.nombre
            session['user_apellido'] = user.apellido
            session['user_email'] = user.email
            session['avatar_color'] = generate_random_color()
            flash('Inicio de sesión exitoso', 'success')
            
            # Redirigir a la página de inicio o a la URL que venía en 'next'
            next_url = request.args.get('next')
            return redirect(next_url or url_for('home'))

        flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html', mensaje_login=mensaje_login, registro_exitoso=registro_exitoso)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            password = data.get('contrasena')

            # Validaciones de entrada
            if not nombre.isalpha() or not apellido.isalpha():
                return jsonify(success=False, message='El nombre y apellido deben contener solo letras.')
            if not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                return jsonify(success=False, message='El correo debe ser una cuenta de Gmail.')
            if User.query.filter_by(email=email).first():
                return jsonify(success=False, message='El correo ya está registrado.')
            password_regex = r'^[A-Z][A-Za-z\d@$!%*#?&]{7,11}$'
            if not re.match(password_regex, password):
                return jsonify(success=False, message='La contraseña debe iniciar con una mayúscula, tener entre 8 y 12 caracteres, incluir al menos un número y un carácter especial.')

            try:
                # Hash de la contraseña y creación del nuevo usuario
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                new_user = User(nombre=nombre, apellido=apellido, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                db.session.rollback()
                return jsonify(success=False, message="Error al crear el usuario en la base de datos."), 500

            try:
                # Generación del token de verificación y envío del correo
                token = generate_confirmation_token(new_user.email)
                expires_at = datetime.utcnow() + timedelta(hours=24)
                verification_token = VerificationToken(token=token, user_id=new_user.user_id, expires_at=expires_at)
                db.session.add(verification_token)
                db.session.commit()

                confirm_url = url_for('confirm_email', token=token, _external=True)
                html = render_template('activate.html', confirm_url=confirm_url)
                subject = "Por favor confirma tu correo"
                send_email(new_user.email, subject, html)

                # Enviar respuesta JSON en lugar de redirigir
                return jsonify(success=True, message="¡Se ha registrado con éxito! Revisa tu correo para verificar tu cuenta.")
            except Exception as e:
                print(f"Error al generar o almacenar el token o al enviar el correo: {e}")
                db.session.rollback()
                return jsonify(success=False, message="Error al generar el token de verificación o enviar el correo."), 500
        else:
            return jsonify(success=False, message="Tipo de contenido no soportado"), 415
    return render_template('Registro.html')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        # Busca el token en la base de datos
        verification_token = VerificationToken.query.filter_by(token=token).first_or_404()

        # Verifica si el token ha expirado
        if verification_token.expires_at < datetime.utcnow():
            # Si el token expiró, eliminar el token y el usuario
            user = verification_token.user
            db.session.delete(verification_token)
            db.session.delete(user)
            db.session.commit()
            flash('El enlace de confirmación ha expirado. Por favor, regístrate de nuevo.', 'danger')
            return redirect(url_for('register'))

        # Si el token es válido y no ha expirado, verificar al usuario y marcar el token como usado
        user = verification_token.user
        user.is_verified = True  # Marcar al usuario como verificado
        verification_token.is_used = True  # Marcar el token como usado
        db.session.commit()  # Guardar los cambios sin eliminar el token

        flash('Has confirmado tu correo electrónico. Gracias! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    except Exception as e:
        print(f"Error al confirmar el token: {e}")
        flash('El token es inválido o ha expirado.', 'danger')
        return redirect(url_for('register'))

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

@app.route('/register_success')
def register_success():
    return render_template('register_success.html')

@app.route('/restricted_page')
def restricted_page():
    user = User.query.get(session['user_id'])
    if not user_has_permission(user, 'access_restricted_page'):
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('home'))
    return render_template('restricted_page.html')

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

from flask import flash

@app.route('/reservas')
def reservas():
    tratamiento = request.args.get('tratamiento', '')
    subservicio = request.args.get('subservicio', '')
    if 'user_id' not in session:
        flash('Debes iniciar sesion para hacer una reserva', 'danger')
        return redirect(url_for('login', next='/reservas'))
    return render_template('Reservaciones.html', tratamiento=tratamiento, subservicio=subservicio)

@app.route('/api/obtener_categorias', methods=['GET'])
def obtener_categorias():
    categorias = Categoria.query.all()
    categorias_json = [{"id": cat.id, "nombre": cat.nombre} for cat in categorias]
    return jsonify(categorias_json)

@app.route('/api/obtener_subservicios', methods=['GET'])
def obtener_subservicios():
    categorias = request.args.get('categorias')
    if not categorias:
        return jsonify({"error": "Categoría no especificada"}), 400
    subservicios = Servicio.query.filter_by(categorias=categorias).all()
    subservicios_json = [{"id": sub.id, "nombre": sub.titulo} for sub in subservicios]
    return jsonify(subservicios_json)

@app.route('/api/obtener_horarios', methods=['GET'])
def obtener_horarios():
    servicio_id = request.args.get('servicio_id')
    dia_nombre = request.args.get('dia')  # Ahora recibimos el día de la semana directamente

    if not servicio_id or not dia_nombre:
        return jsonify({"error": "Faltan parámetros"}), 400

    # Buscar el ID del día en la tabla 'dias' usando el nombre del día
    dia = Dia.query.filter_by(nombre=dia_nombre).first()
    if not dia:
        return jsonify({"error": "Día no encontrado"}), 404

    # Obtener los horarios del servicio y día especificados
    horarios = Horario.query.filter_by(servicio_id=servicio_id, dia_id=dia.id).all()
    horarios_json = []
    for horario in horarios:
        bloque_hora = BloqueHora.query.get(horario.bloque_hora_id)
        if bloque_hora:
            horarios_json.append({
                "id": horario.id,
                "hora_inicio": bloque_hora.hora_inicio,
                "hora_fin": bloque_hora.hora_fin
            })

    return jsonify({"horarios": horarios_json})

def obtener_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
    return dias_semana[fecha_dt.weekday()]

@app.route('/api/reserva', methods=['POST'])
def guardar_reserva():
    try:
        data = request.get_json()
        # Obtener user_id directamente de la sesión
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Usuario no identificado. Por favor, inicie sesión para hacer una reserva."}), 403

        servicio = data.get('servicio')
        fecha_reserva = data.get('fecha_reserva')
        fecha_uso = data.get('fecha_uso')
        nombre_cliente = data.get('nombre_cliente')

        # Validación de todos los campos
        if not all([servicio, fecha_reserva, fecha_uso, nombre_cliente]):
            return jsonify({"error": "Todos los campos son requeridos"}), 400

        # Validación del formato de fecha
        try:
            fecha_reserva = datetime.strptime(fecha_reserva, '%Y-%m-%d').date()
            fecha_uso = datetime.strptime(fecha_uso, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

        # Verificación de usuario existente en la base de datos
        usuario = db.session.get(User, user_id)
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        # Creación de la reserva
        nueva_reserva = Reserva(
            user_id=user_id,
            servicio=servicio,
            fecha_reserva=fecha_reserva,
            fecha_uso=fecha_uso,
            nombre_cliente=nombre_cliente
        )
        db.session.add(nueva_reserva)
        db.session.commit()

        # Envío de correo de confirmación
        try:
            enviar_correo_reserva(usuario.email, nombre_cliente, servicio, fecha_reserva, fecha_uso)
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            return jsonify({"error": "Reserva guardada, pero ocurrió un error al enviar el correo."}), 500
        
        return jsonify({"message": "Reserva guardada exitosamente"}), 201

    except Exception as e:
        print(f"Error al guardar la reserva: {e}")
        return jsonify({"error": f"Ocurrió un error en el servidor: {e}"}), 500

def enviar_correo_reserva(email, nombre_cliente, servicio, fecha_reserva, horario):
    try:
        html = render_template('reserva_confirmacion.html', 
                               nombre_cliente=nombre_cliente, 
                               servicio=servicio, 
                               fecha_reserva=fecha_reserva, 
                               horario=horario)
        msg = Message(subject="Confirmación de su Reserva",
                      recipients=[email],
                      html=html,
                      sender=app.config['MAIL_USERNAME'])
        mail.send(msg)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo de reserva: {e}")


@app.route('/historial_reservas')
def historial_reservas():
    if 'user_id' not in session:
        return redirect(url_for('login', next=url_for('historial_reservas')))
    user_id = session['user_id']
    reservas = Reserva.query.filter_by(user_id=user_id).order_by(Reserva.fecha_reserva.desc()).all()
    return render_template('historial_reservas.html', reservas=reservas)

@app.route('/carrito')
def carrito():
    user_name = session.get('user_name', None)
    user_apellido = session.get('user_apellido', None)
    user_email = session.get('user_email', None)
    avatar_color = session.get('avatar_color', None)
    return render_template('Carrito.html', user_name=user_name, user_apellido=user_apellido, user_email=user_email, avatar_color=avatar_color)

if __name__ == '__main__':
    app.run(debug=True)














