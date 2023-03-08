from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    
    def get(self):
        query: Query = conexion.session.query(Nivel)

        resultado = query.all()



        dto = NivelDto()
        niveles = dto.dump(resultado, many=True)

       # print(resultado[0].numero)
       # print(resultado[0].descripcion)

       # niveles = []

       # for nivel in resultado:
       #     niveles.append(
       #     {
       #             'id' : nivel.id,
       #             'numero': nivel.numero,
       #             'descripcion': nivel.descripcion
       #     }) 
             
        return{
                'content': niveles
            }
    


    def post(self):
        data = request.json

        dto = NivelDto()

        try:

           data_validada =  dto.load(data)
           print(data_validada)

           nuevo_nivel = Nivel(numero=data_validada.get('numero'), descripcion=data_validada.get('descripcion'))

       
           conexion.session.add(nuevo_nivel)
        
           conexion.session.commit()

           return {
             'message' : 'Nivel creado exitosameente'
          }, 201
    
        except Exception as error:
           return {
                'message' : 'Error al crear nivel',
                'content': error.args
            } 
         
class UnNivelController(Resource):
    def get(self, id):

        query: Query = conexion.session.query(Nivel)
        nivel_encontrado = query.filter_by(id= id).first()

        if nivel_encontrado is None:
            return {
                'message': 'El nivel no existe'
            }

        dto = NivelDto()
        resultado = dto.dump(nivel_encontrado)

       
        return {
            'message': resultado
        }
    
