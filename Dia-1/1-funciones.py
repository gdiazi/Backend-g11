def saludar(nombre):
    saludo = 'Hola {}' .format(nombre)
    print(saludo)


saludar('Eduardo')


def saludar_varios(*args):
    # cunado nosotros colocamos en un parametro el '*' significa que no hay limite de ese parametro

    print(args)

    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)

saludar_varios('Roxsana', 'Juana', 'Martin', 'Roberto')
saludar_varios('Pedro', 'Luis')    
saludar_varios()
saludar_varios('Eduardo', 20, True, 10.5)   

def informacion_usuario(**kwargs):
    # kwargs > keboard argument o se le pasan parametros por llaves
    print(kwargs)


    print(kwargs.get('estatura', 'NO HAAAAY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')


informacion_usuario(nombre='Eduardo', edad=30, esta_civil='soltero', estatura= 1.88)
informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Colombiana', fecha_nacimiento= '31/06/1999')

print('ADIOOOOOS')

#recibir dos valores y hacer la division (dividendo / divisor) y retornar su resultado

def dividir(dividendo, divisor):

        try:
            resultado = dividendo / divisor
            return resultado
        except ZeroDivisionError:
            return 'No puede haber division entre 0' 
        except TypeError:
            return 'Las divisiones pueden ser entre 2 numeros'
        except:
            return 'Error desconocido'         

valor = dividir(10,5) 
print(valor)

valor = dividir(10,0)
print(valor)


try:
    valor = dividir(5, )
    print(valor)
except TypeError:
    print('Estuvo mal llamar asi')    
