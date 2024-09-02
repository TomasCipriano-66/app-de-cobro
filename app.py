from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'u2jsmodvktmxthwk'
app.config['MYSQL_PASSWORD'] = 'JTSZ6HR3AMgW3HDo7ykz'
app.config['MYSQL_HOST'] = 'bwpeifpsxajflfti7mrf-mysql.services.clever-cloud.com' 
app.config['MYSQL_DB'] = 'bwpeifpsxajflfti7mrf'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')


# --------------SECCION ADMINS----------------

#cargar tablas
@app.route('/ADMIN')
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Inscripcion')
    data1 = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault')
    data2 = cur.fetchall()
    cur.close()
    return render_template('ADMIN.html', Table1_inf = data1, Table2_inf = data2)

#eliminar un equipo de la DB
@app.route('/delete/<string:id>')
def delete_team(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Inscripcion WHERE id = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))




if __name__ == '__main__':
    app.run(port=2500, debug=True)
