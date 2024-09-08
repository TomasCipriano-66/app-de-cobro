from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'  # Necesaria para manejar sesiones

# Datos de ejemplo de productos
productos = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 2000, 'img': 'static/images/product1.jpg'},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 5000, 'img': 'static/images/product2.jpg'},
    {'id': 3, 'nombre': 'Producto 3', 'precio': 3000, 'img': 'static/images/product3.jpg'}
]

@app.route('/')
def home():
    return render_template('home.html', productos=productos)

@app.route('/agregar/<int:producto_id>')
def agregar_al_carrito(producto_id):
    # Buscar el producto seleccionado
    producto_seleccionado = next((item for item in productos if item['id'] == producto_id), None)

    if producto_seleccionado:
        # Obtener el carrito de la sesión, o crear uno nuevo si no existe
        if 'carrito' not in session:
            session['carrito'] = []

        carrito = session['carrito']

        # Verificar si el producto ya está en el carrito
        producto_en_carrito = next((item for item in carrito if item['id'] == producto_id), None)

        if producto_en_carrito:
            # Si ya está en el carrito, aumentar la cantidad
            producto_en_carrito['cantidad'] += 1
        else:
            # Si no está, agregarlo al carrito con cantidad 1
            producto_seleccionado['cantidad'] = 1
            carrito.append(producto_seleccionado)

        # Guardar el carrito en la sesión
        session['carrito'] = carrito

    return redirect(url_for('carrito'))

@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

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
