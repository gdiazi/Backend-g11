from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api

from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController
from controllers.nivel_controller import NivelController, UnNivelController


load_dotenv()



app = Flask(__name__)
# print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

flask_api = Api(app=app)

conexion.init_app(app)

Migrate(app=app, db=conexion)

flask_api.add_resource(NivelController, '/nivel')
flask_api.add_resource(UnNivelController, '/nivel/<id>')

if __name__ == '__main__':
    app.run(debug=True)


