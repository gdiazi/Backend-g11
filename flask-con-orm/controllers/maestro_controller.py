from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto


class MaestroController(Resource):

    def get(self):
        query: Query = conexion.session.query(Maestro)

        resultado = query.all()

        dto = MaestroDto()

        maestros = dto.dump(resultado, many=True)

        return {
            'content': maestros
        }

    def post(self):
        data = request.json
        dto = MaestroDto()

        try:

            data_validada = dto.load(data)
            print(data_validada)

            nuevo_maestro = Maestro(nombre=data_validada.get('nombre'), apellido=data_validada.get(
                'apellido'), correo=data_validada.get('correo'), direccion=data_validada.get('direccion'))

            conexion.session.add(nuevo_maestro)

            conexion.session.commit()
            return {
                'message': 'maestro creado exitosamente'
            }, 201

        except Exception as error:
                   return {
                 'message': 'error al crear maestro',
                 'content': error.args
             }


