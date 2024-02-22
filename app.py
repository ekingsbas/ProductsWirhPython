from flask import Flask, request, jsonify
from sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos para SQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://usuario:contraseña@nombre_servidor/nombre_base_de_datos?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

# Define modelos de datos utilizando SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
# Define las rutas de tu API y las funciones de vista asociadas
@app.route('/users', methods=['GET'])
def get_users():
    # Código para obtener usuarios de la base de datos
    users = User.query.all()
    output = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': output})

@app.route('/users', methods=['POST'])
def create_user():
    # Código para crear un nuevo usuario en la base de datos
    return jsonify({'message': 'User created successfully'})

# Inicia tu aplicación Flask para que pueda manejar solicitudes entrantes desde el navegador
if __name__ == '__main__':
    app.run(debug=True)