


# def suma(a, b):
#    return a + b
  #  return resultado
#    print(resultado)
#resultado_suma = suma(2, 3)  
#print(resultado_suma) 



# def resta(a, b):
#    return a-b

# def multiplicacion(a, b):
#    return a * b

# def division(a, b):
#    return a / b   

#print(division(5, 2))

#print('¿Que operacion desea realizar?')
#opcion = input('Indicar opeeración matematica:')
#print('La operación que solicito es' + opcion)


# a = 5
#b = 6
 
# def Calcular():
#    if suma(a, b):
#        return a + b

#    elif resta(a, b):
#        return a-b
#    elif multiplicacion(a, b):
#         return a * b 
#    elif  division(a, b):
#           return a / b     




#2print(Calcular())


#n1 = float(input("Introduce tu primer número: ") )
#n2 = float(input("Introduce tu segundo número: ") )

#opcion = 0
#while True:
#    print("""
#    Dime, ¿qué quieres hacer?
    
#    1) Sumar los dos números
#    2) Restar los dos números
#    3) Multiplicar los dos números
#    4) Cambiar los números elegidos
#    5) Apagar calculadora
#    """)
#    opcion = int(input("Elige una opción: ") )     

#    if opcion == 1:
#        print(" ")
#        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
#    elif opcion == 2:
#        print(" ")
#        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
#    elif opcion == 3:
#        print(" ")
#        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
#    elif opcion == 4:
#        n1 = float(input("Introduce tu primer número: ") )
#        n2 = float(input("Introduce tu segundo número: ") )
#    elif opcion == 5:
#        break
#    else:
#        print("Opción incorrecta")




def suma(a, b):
    return a + b

# resultado_suma = suma(1, 2)
# print(resultado_suma)

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    if operacion == 'suma':
        return f'El resultado de la {operacion} es: {suma(valor_1, valor_2)}'
    elif operacion == 'resta':
        return f'El resultado de la {operacion} es: {resta(valor_1, valor_2)}'
    else:
        return 'La operación no existe'

operacion = input('Ingrese el tipo de operacion: ')
valor_1 = int(input('Ingrese el primer número: '))
valor_2 = int(input('Ingrese el segundo número: '))

resultado = calcularResultadoPorOperacion(operacion, valor_1, valor_2)

print(resultado)