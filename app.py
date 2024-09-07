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
    cursor.execute("SELECT nombre, precio, stock, img FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    return render_template('home.html', productos=productos)

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

if __name__ == '__main__':
    app.run(debug=True)
