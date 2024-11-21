# App de Cobro Prototipo

Una aplicación web sencilla e intuitiva para realizar pagos en línea. La app permite a los usuarios agregar productos a un carrito, revisar su orden, y completar el pago mediante la integración con **Mercado Pago** para mayor seguridad. La aplicación está construida con **Python**, **Flask**, **MySQL** y usa la API de **Mercado Pago** para procesar pagos.

## Tecnologías Principales

- **Python**: Lenguaje de programación para el backend.
- **Flask**: Micro-framework para crear la aplicación web.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos MySQL.
- **MySQL**: Sistema de gestión de bases de datos para almacenar información de usuarios, productos, y transacciones.
- **Mercado Pago API**: Para manejar los pagos de manera segura y eficiente.
- **HTML/CSS/JavaScript**: Para la interfaz de usuario del lado del cliente.

## Funcionalidades

### 1. **Gestión de Carrito de Compras**
- Los usuarios pueden agregar productos al carrito.
- El carrito es visible en todo momento, lo que permite a los usuarios agregar o eliminar productos fácilmente.
- Los productos se muestran con su nombre, descripción, precio y cantidad.
- Se calcula el total del carrito en tiempo real, mostrando el precio final con base en los productos seleccionados.

### 2. **Login y Registro de Usuarios**
- Los usuarios pueden registrarse y loguearse en la aplicación.
- La autenticación de los usuarios se maneja mediante sesiones seguras.
- Solo los usuarios registrados pueden proceder al proceso de pago.

### 3. **Proceso de Pago**
- Una vez el usuario revise su carrito, puede proceder a pagar.
- El pago se realiza de manera segura mediante la **API de Mercado Pago**, que maneja las transacciones.
- La aplicación genera un enlace de pago que se redirige al usuario a Mercado Pago, donde se puede completar el pago con tarjetas de crédito, débito o métodos de pago locales.
- Una vez el pago es confirmado, el usuario es redirigido de vuelta a la aplicación con un resumen de la transacción y estado del pago.


### Paso 1: Clona el Repositorio

```bash
git clone https://github.com/tuusuario/copa-renault.git
cd copa-renault
```

### Paso 2: Instala las Dependencias

Para instalar las dependencias del proyecto, usa los siguientes comandos:

```bash
pip install Flask
pip install Flask-MySQLdb
```

### Paso 3: Ejecuta la APP

Para ejecutar la aplicación, utiliza el siguiente comando en la carpeta del proyecto:

```bash
python app.py
```
