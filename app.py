from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'unywje4ax5puclwk'
app.config['MYSQL_PASSWORD'] = 'Uz9KmlHRoqhzEMEQAuAl'
app.config['MYSQL_HOST'] = 'bgbng8uouisbf7l4ajx0-mysql.services.clever-cloud.com'
app.config['MYSQL_DB'] = 'bgbng8uouisbf7l4ajx0'
mysql = MySQL(app)

@app.route('/')
def home():
    # Conectar a la base de datos y obtener productos
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, nombre, precio, stock, img FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    return render_template('home.html', productos=productos)

@app.route('/carrito')
def carrito():
    # Aquí puedes obtener los datos del carrito desde la sesión o una base de datos
    # Simulando un carrito
    carrito = [
        {'nombre': 'Producto 1', 'cantidad': 1, 'precio': 2000},
        {'nombre': 'Producto 2', 'cantidad': 3, 'precio': 5000},
    ]
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/procesar_compra', methods=['POST'])
def procesar_compra():
    carrito = [
        {'nombre': 'Producto 1', 'cantidad': 1, 'precio': 2000},
        {'nombre': 'Producto 2', 'cantidad': 3, 'precio': 5000},
    ]
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    
    # Insertar la compra en la tabla "compras"
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO compras (total) VALUES (%s)", (total,))
    compra_id = cursor.lastrowid
    
    # Insertar los productos comprados
    for item in carrito:
        cursor.execute(
            "INSERT INTO productos_comprados (compra_id, nombre, cantidad, precio) VALUES (%s, %s, %s, %s)",
            (compra_id, item['nombre'], item['cantidad'], item['precio'])
        )
    
    # Confirmar los cambios
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('carrito'))

if __name__ == '__main__':
    app.run(debug=True)
