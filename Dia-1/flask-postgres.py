from flask import Flask, request
from psycopg2 import connect
from flask_cors import CORS

app = Flask(__name__)

app = Flask(__name__)
CORS(app, methods = ['GET', 'POST', 'PUT', 'DELETE'], origins = ['http://localhost:5500', 'http://127.0.0.1:5500'])

# me conecto a la bd
conexion = connect(host='localhost', database='pruebas', user='postgres', password='q1w2e3r4', port=5433 )

@app.route('/', methods = ['GET'])
def inicial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods = ['GET', 'POST'])
def alumnos():
    if request.method == 'GET':
        # creo un cursor que es el responsable de hacer lecturas y escrituras a la bd
        cursor = conexion.cursor()
        
        # ejecuto la query
        cursor.execute('SELECT * FROM alumnos;')

        # extraigo la informacion de la ejecucion de la query
        resultado = cursor.fetchall()

        print(resultado)
        alumnos_resultado = []

        for alumno in resultado:
            info_alumno = {
                'id': alumno[0],
                'nombre': alumno[1],
                'apellido': alumno[2],
                'sexo': alumno[3],
                'fecha_creacion': alumno[4],
                'matriculado': alumno[5]
            }

            alumnos_resultado.append(info_alumno)
            print(info_alumno)
        return {
            'message': alumnos_resultado
        }
    
    elif request.method == 'POST':
        data = request.json
        print(data)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ALUMNOS (nombre, apellido, sexo, matriculado) VALUES (%s, %s, %s)",(
            data.get('nombre'), data.get('apellido'), data.get('sexo'), data.get('matriculado')
        ))

        conexion.commit()


        return {
            'message': 'Alumno ingresado exitosamente'
        }
    
def validar_alumno(id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id,))

    alumno_resultado = cursor.fetchone()

    cursor.close()
    print(alumno_resultado)
    return alumno_resultado

@app.route("/alumno/<int:id>", methods = ['GET', 'PUT', 'DELETE'])

def gestion_alumno(id):
    if request.method == 'GET':

        alumno = validar_alumno(id)  
      
        if alumno is None:

            return{
                'message': 'Alumno no encontrado'
            }   
         
        else:
            info_alumno = {
                'id': alumno[0],
                'nombre': alumno[1],
                'apellido': alumno[2],
                'sexo': alumno[3],
                'fecha_creacion': alumno[4],
                'matriculado': alumno[5]
            }

        return{
            'content': info_alumno
        } 
       
    elif request.method == 'PUT':
        alumno_resultado = validar_alumno(id)

        if alumno_resultado is None:
            return{
                'message': 'Alumno no existe'
            }
        else:
            data=request.get_json()
            cursor = conexion.cursor()       

            cursor.execute("UPDATE alumnos SET nombre= %s, apellido= %s, sexo= %s, fecha_creacion= CURRENT_TIMESTAMP, matriculado= %s WHERE id=%s", [
                data.get('nombre'),
                data.get('apellido'),
                data.get('sexo'),
                data.get('matriculado'),
             
                alumno[0] # id del producto
            ])
            conexion.commit()
            conexion.close()

        return {
                'message': 'Alumno actualizado exitosamente'
            }
    
    elif request.method == 'DELETE':
            alumno_resultado = validar_alumno(id)
           
            if alumno is None:
                return {
                    'message': 'Alumno no existe'
                }
            else:
                

             return{
                'message':'el alumno existe'
             }
        
    else:   
             
             cursor = conexion.cursor()
             conexion.execute("DELETE FROM alumnos WHERE id = %s", [id])

             conexion.commit()
             conexion.close()


    return{
                'message': 'Alumno eliminado exitosamente'
          }
       # elif request.method == 'PUT':
        
        #Reibir informacion del body y esta modificar la data del alumno, primero validar si el alumno existe, si no existe no hacer ninguna modifcacion,si existe hacer la modificaicon

    #    pass

   # elif request.method == 'DELETE':
        
        # Reicibir el id por la url y validar si el alum,no existe, si existe eliminarlo(hacer delete) caso contrario indicar que el alumno no existe


       # print(alumno)
       # return{
       #      'message': id
       #  }


if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)