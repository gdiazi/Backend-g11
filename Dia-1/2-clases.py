class Persona:

#Cuando una variable se dedefine dentro de una clase pasa a lamarse ATRIBUTO
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'LEO'



    def sumar(self, *args):

        # cuando una funcion se declara o se define dentro de una clase pasa a llamarse METODO
        total = 0

        for numero in args: 
            total = total + numero
        return total

    def saludar(self, nombre):
       return 'Hola {}' .format(nombre)



persona1 = Persona()
persona2 = Persona()     

persona1.peso = 70
persona2.peso = 50
 
print(persona1.peso)
print(persona2.peso)


resultado1 = persona1.sumar(10, 5, 41, 526, 489, 63)
resultado2 = persona1.sumar(10, 5, 41, 527, 489, 63)

print(resultado1)
print(resultado2)