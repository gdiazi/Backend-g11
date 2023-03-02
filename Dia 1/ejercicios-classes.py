#Crear una Clase Operaciones con sus respecctivos metodos
#(Sumar, restar, multiplicar y dividr). Esta clase recibira 2 parametros

 # def __init__(self, a, b):
 #      self.suma = a + b
 #      self.resta = a - b
 #      self.multiplica = a * b
 #      self.division = a / b


#class operaciones:

#   def __init__(self, a, b):

#        self.num1 = a
#        self.num2 = a

#   def suma(self):
 #           return self.a + self.b

#   def resta(self):
#            return self.a - self.b 


#   resul = operaciones(30,20)
   #print(resul.suma())

    # resultado_suma = suma(1, 2)
    # print(resultado_suma)

from pprint import pprint

class OperacionesMatematicas:

    def __init__(self, valor_1, valor_2):
        self.a = valor_1
        self.b = valor_2
      

    def sumar(self):
        return self.a + self.b 


    def restar(self):
        return self.a - self.b     

    def multiplicar(self):
        return self.a * self.b     

    def dividir(self):
        return self.__redondear(self.a / self.b)

    def __redondear(self, numero):     
        return round(numero, 2)


operaciones = OperacionesMatematicas(5, 3)

  # print(operaciones.dividir())


# Crear una clase usuario que reciba los datos de usuario
# (nombre, edad, dni, estatura, estado civil) y convertir estos
# datos en un diccionario


class Usuario:

    def __init__(self, nombre, edad, dni, estatura, estado) -> None:
        self.nom = nombre
        self.anio = edad
        self.docu = dni
        self.talla = estatura
        self.estado = estado

    def diccionario(self):
        return {

        "nombre": self.nom,
         "edad": self.anio,
         "dni": self.docu,
         "estatura": self.talla,
         "estado": self.estado

        }

Usuario = Usuario("Guille", 25, 7415751, 160, "S")   
pprint(Usuario.diccionario())  


