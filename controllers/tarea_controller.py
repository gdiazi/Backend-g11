from flask_restful import Resource, request
from sqlalchemy.orm import Query
from sqlalchemy import and_, or_, Enum
from flask_jwt_extended import jwt_required, get_jwt_identity
from dtos.tarea_dto import TareaDto
from models.tarea_model import Tarea, EstadoTareaEnum
from bd import conexion


class TareasController(Resource):
    @jwt_required()
    def post(self):
        usuario_id = get_jwt_identity()
        data = request.json
        dto = TareaDto()
        try:
            data_validada = dto.load(data)
            nueva_tarea = Tarea(**data_validada, usuarioId = usuario_id)
            conexion.session.add(nueva_tarea)
            conexion.session.commit()

            return{
                'message': 'Se agrego exitosamente'
            }
        except Exception as error:
            return{
                'message': 'Error',
                'content': error.args
            }
            

        
    @jwt_required()
    def get(self):
      
        usuario_id = get_jwt_identity()
        query: Query = conexion.session.query(Tarea)
     
        print(usuario_id)

        tareas_usuario: Tarea = query.filter_by(usuarioId = usuario_id).all()
        print(tareas_usuario)

        dto = TareaDto()

        data = dto.dump(tareas_usuario, many=True)

        return{
            'message': 'El usuario existe',
            'content': data
        }        
  
   # def get(self):
   #     pass
        
        #  devolver toddas las tareas del usuario
        # Utilizando query params poder reicibir el nombre, fecha_vencimiento o el estado y devolver solamente
        #  esas tareas con filtros especializados solo del usuario
        # /tarea?nombre=Ir a la piscina
        # /tarea?estado=REALIZANDOSE
        # /tarea?fecha_vencimiento=2023-07-31 14:55:25
        # /tarea?nombre=Playa&estado=PENDIENTE
        # if - elif -else


class ConsultaController(Resource):
    @jwt_required()
    def get(self):
        usuario_id = get_jwt_identity()
        print(usuario_id)
    
        
        nombre = request.args.get('nombre')
        estado = request.args.get('estado')
        fechaVencimiento = request.args.get('fecha_vencimiento')

        nombreTarea = "%{}%".format(nombre)
        fechaVencimiento = "%{}%".format(fechaVencimiento)
        print(fechaVencimiento)

        query: Query = conexion.session.query(Tarea)
        tarea_encontrada: Tarea = query.filter(and_(Tarea.usuarioId == usuario_id, 
                                                Tarea.estado == EstadoTareaEnum(estado), 
                                                Tarea.fechaVencimiento == fechaVencimiento, 
                                                Tarea.nombre.like(nombreTarea))).all()

        print(tarea_encontrada)

        dto = TareaDto()
        data = dto.dump(tarea_encontrada, many=True)

        return{
            'content': data
        }



#class TareasFecha(Resource):
#        def get(self):
#            data = request.json
          
           
            
        #  try:
    
 #           data_validada = dto.load(data) 
 #           query:Query = conexion.session.query(Tarea)
 #           tarea_encontrada:Tarea = query.filter_by(fecha = data_validada.get(fecha = (2023, 7, 31)).all())

 #           dto = TareaDto()

 #           data = dto.dump(tarea_encontrada)

 #           return{
 #                   'content': data
 #               }     
        


#class TareasEstado(Resource):
#        def get(self):
#            data = request.json
          
           
            
        #  try:
    
 #           data_validada = dto.load(data) 
 #           query:Query = conexion.session.query(Tarea)
 #         #  tarea_encontrada:Tarea = query.filter_by(fecha = data_validada.get(fecha = (2023, 7, 31)).all())

 #           tarea_encontrada:Tarea = query.filter_by(estado).filter(and_(estadotareaenum.like('REALIZANDOSE')))

 #           dto = TareaDto()

 #           data = dto.dump(tarea_encontrada)

 #           return{
 #                   'content': data
 #               }     



