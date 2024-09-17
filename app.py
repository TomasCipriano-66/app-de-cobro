from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'sope_con_pure'


app.config['MYSQL_USER'] = 'unywje4ax5puclwk'
app.config['MYSQL_PASSWORD'] = 'Uz9KmlHRoqhzEMEQAuAl'
app.config['MYSQL_HOST'] = 'bgbng8uouisbf7l4ajx0-mysql.services.clever-cloud.com'
app.config['MYSQL_DB'] = 'bgbng8uouisbf7l4ajx0'
mysql = MySQL(app)




# Datos de ejemplo de productos
@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre, precio, img FROM productos")
    productos_db = cursor.fetchall()
    cursor.close()

    # Convertir la salida de la base de datos en una lista de diccionarios
    productos = []
    for producto in productos_db:
        productos.append({
            'nombre': producto[0],
            'precio': producto[1],
            'img': producto[2]
        })

    return render_template('home.html', productos=productos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticación para login
        username = request.form['username']
        password = request.form['password']
        # Aquí iría la verificación de credenciales en la base de datos
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Lógica para el registro de usuarios
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Aquí iría la lógica para registrar el usuario en la base de datos
        return redirect(url_for('home'))
    return render_template('signup.html')



@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])

    # Asegurarse de que cada producto tenga stock, en caso de que falte
    for item in carrito:
        if 'stock' not in item:
            # Aquí podrías consultar el stock de la base de datos nuevamente si es necesario
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT stock FROM productos WHERE nombre = %s", (item['nombre'],))
            stock = cursor.fetchone()
            cursor.close()
            if stock:
                item['stock'] = stock[0]

    # Actualizar la sesión con los cambios
    session['carrito'] = carrito

    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)



@app.route('/agregar/<producto_nombre>')
def agregar_al_carrito(producto_nombre):
    # Consultar el producto por nombre en la base de datos
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre, precio, img, stock FROM productos WHERE nombre = %s", (producto_nombre,))
    producto = cursor.fetchone()
    cursor.close()

    if producto:
        producto_seleccionado = {
            'nombre': producto[0],
            'precio': producto[1],
            'img': producto[2],
            'stock': producto[3]  # Asegurarse de que stock se incluye
        }

        # Obtener el carrito de la sesión, o crear uno nuevo si no existe
        if 'carrito' not in session:
            session['carrito'] = []

        carrito = session['carrito']

        # Verificar si el producto ya está en el carrito
        producto_en_carrito = next((item for item in carrito if item['nombre'] == producto_nombre), None)

        if producto_en_carrito:
            # Verificar si se puede agregar más según el stock disponible
            if producto_en_carrito['cantidad'] < producto_seleccionado['stock']:
                producto_en_carrito['cantidad'] += 1
        else:
            # Si no está, agregarlo al carrito con cantidad 1 y asegurar que tenga el stock
            producto_seleccionado['cantidad'] = 1
            carrito.append(producto_seleccionado)

        # Guardar el carrito en la sesión
        session['carrito'] = carrito

    return redirect(url_for('carrito'))



@app.route('/sumar/<producto_nombre>')
def sumar(producto_nombre):
    carrito = session.get('carrito', [])

    # Buscar el producto en el carrito
    producto_en_carrito = next((item for item in carrito if item['nombre'] == producto_nombre), None)

    if producto_en_carrito:
        # Solo sumar si no excede el stock disponible
        if producto_en_carrito['cantidad'] < producto_en_carrito['stock']:
            producto_en_carrito['cantidad'] += 1

    session['carrito'] = carrito
    return redirect(url_for('carrito'))


@app.route('/restar/<producto_nombre>')
def restar(producto_nombre):
    carrito = session.get('carrito', [])

    # Buscar el producto en el carrito
    producto_en_carrito = next((item for item in carrito if item['nombre'] == producto_nombre), None)

    if producto_en_carrito and producto_en_carrito['cantidad'] > 1:
        # Decrementar la cantidad si es mayor a 1
        producto_en_carrito['cantidad'] -= 1
    elif producto_en_carrito and producto_en_carrito['cantidad'] == 1:
        # Eliminar el producto si la cantidad es 1 y se presiona restar
        carrito.remove(producto_en_carrito)

    session['carrito'] = carrito
    return redirect(url_for('carrito'))


@app.route('/vaciar_carrito')
def vaciar_carrito():
    session.pop('carrito', None)  # Eliminar el carrito de la sesión
    return redirect(url_for('carrito'))

@app.route('/procesar_compra', methods=['POST'])
def procesar_compra():
    # Aquí podrías procesar el pago o simplemente vaciar el carrito
    session.pop('carrito', None)  # Vaciar el carrito después de la compra
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

