from camelcase import CamelCase

instancia = CamelCase()

texto = 'hooa como estas'



resultado = instancia.hump(texto)
print(resultado)


def sumar(num1: int, num2:int) -> int:
    return num1 + num2
sumar(10,5)    