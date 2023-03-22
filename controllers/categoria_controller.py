from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
from uuid import uuid4
from dtos.categoria_dto import CategoriaDto
from models.categoria_model import Categoria
from db import conexion
from sqlalchemy.orm import Query 


class ImagenesController(Resource):
    def post(self):
        
        print(request.form)
        print(request.files)

        imagen = request.files.get('imagen')
       
        print(imagen.filename)

        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)    
        imagen.save(path.join('imagenes', nombre_seguro))


        return{
            'messsage': 'Categoria creada exisotsamente'

        }
    

    def get(self, nombre):
        
          try:
                   
             return send_file(path.join('imagenes', nombre))
          
          except FileNotFoundError:
             return send_file(path.join('imagenes', 'not_found.jpg'))

class CategoriasController(Resource):       
    def post(self):

        mimetype_valido = ['image/svg+xml', 'image/webp', 'image/png', 'image/jpeg']
        mimetype_valido = 'image/'
        data = request.form.to_dict()
        try:
        
            imagen = request.files.get('imagen')
            print(imagen.filename)

            if mimetype_valido not in imagen.mimetype:
                  
                  
                    raise Exception('No es valido')
                
           
            # return{
            # 'message' : 'No es valido'       
            #   }
          
           
            dto = CategoriaDto()
            nombre = secure_filename(uuid4().hex +'_'+imagen.filename)

            data['imagen'] = 'imagenes/' + nombre
            data_serializada = dto.load(data)

            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)

            imagen.save(path.join('imagenes', nombre))    
            conexion.session.commit()

            return{
                        'message' : 'Categoria creada exitosaMENTE'       
                 }
        
        except Exception as error:
            conexion.session.rollback()
        return{
                      'message': 'Error al crear',
                      'content': error.args
                 }
             # print(imagen.mimetype)
        

    def get(self):
        query: Query = conexion.session.query(Categoria)
        resultado = query.all()
        dto = CategoriaDto()
        data = dto.dump(resultado, many=True)

        return{
            'content': data
        }
    

