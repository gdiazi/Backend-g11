def cacularResultadoPorOperacion(operacion, valor_1, valor_2):
    
    if operacion == 'suma':
        return suma(valor_1, valor_2)
    elif operacion == 'resta':
        return resta(valor_1, valor_2)    
    else:
        return 'La operacion no existe' 

    operacion =  input('Ingrese el tipo de operacion')       
    valor_1 = int(input('Ingrese el primer numero: '))
    valor_2 = int(input('Ingrese el primer numero: '))

    resultado = cacularResultadoPorOperacion(operacion, valor_1, valor_2)
    print('El resultado de la operacion es' + resultado)
