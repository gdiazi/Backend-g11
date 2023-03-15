from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

from controllers.usuario_controller import UsuariosController, LoginController, PerfilController
from controllers.tarea_controller import TareasController, ConsultaController

from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:q1w2e3r4@localhost:5433/tareas'

app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1,minutes=10)

api = Api(app)

conexion.init_app(app)

Migrate(app = app, db = conexion)
JWTManager(app)

api.add_resource(UsuariosController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')
api.add_resource(TareasController, '/tareas')

api.add_resource(ConsultaController, '/tarea', endpoint='tarea')

if __name__ == '__main__':
    app.run(debug=True)

