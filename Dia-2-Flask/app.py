from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return "Binevnidos a mi primer API con Flask 😀"

@app.route("/alumno")
def alumno():
    return{
        'nombre': 'Eduardo',
        'edad': 30,
        'promedio' : 18
    }


lista_alumnos = [
    
    {
        'nombre': 'Eduardo',
        'edad': 30,
        'promedio' : 18
    },
      {
        'nombre': 'Guillermo',
        'edad': 25,
        'promedio' : 18
    }

    ]


@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def alumnos():
    print(request.method)
    if request.method == 'GET':
        return lista_alumnos
    elif request.method == 'POST':
        lista_alumnos.append(request.json)
        # metodo para obtener el body (request.json) o (request.get_json)
        
    return lista_alumnos

@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno['nombre'] == nombre:
            return alumno
    return {
        'message': 'El alumno no existe'
     }


@app.route("/html")
def html():
   edad = 10

   return render_template('index.html', edad=edad)

   # return "<button>Dame click</button>"
@app.route("/form-data", methods=['POST'])
def form_data():
    print(request.form)
    return 'Form data recibido existosamente'

@app.route("/files", methods=['POST'])
def files():

        file_str = request.files['foto'].read().decode('utf8')
        f = open('archivo.txt', "w") 
        f.write(file_str)
        # f= open(request.files['foto'].read().decode(), "w")
        return 'archivo recibido exitosamente'

# debug => Si realizamos algun cambio podemos verlo en tiempo real ( sere iniciara el server)
app.run(debug=True)

