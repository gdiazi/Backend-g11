class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print('Buenos dias')    



class Beneficio:
    def __init__(self, detalle):
        self.detalle = detalle
    def mostrar_beneficios(self):
        return{
            'detalle': self.detalle
        }


class Alumno(Persona):

    def __init__(self, nombre, apellido, grado):
        self.grado = grado
        super().__init__(nombre, apellido)

        

 
     #   print(saludo.padre + 'Yo soy un alumno')

    def dar_vueltas(self):
            print('Dando vueltas....')


class Docente(Persona, Beneficio):
    def __init__(self, nombre, apellido, seguro_social, detalle):       
        self.seguro_social = seguro_social

        Persona.__init__(self, nombre, apellido)
        Beneficio.__init__(self, detalle)


    def evaluar(self):
        print('Evaluando...')        


eduardo = Alumno('eduardo', 'de rivero', 'quinto')
paolo = Docente('paolo', 'soncco', '1596425')
  

eduardo.saludar()
paolo.saludar()


print(paolo.mostrar_beneficios())
print(eduardo.nombnre)

