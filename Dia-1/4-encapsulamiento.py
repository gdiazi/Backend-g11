class Producto:
        def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            self.fecha_vencimiento = fecha_vencimiento
            
            self.__ganancia = 0.3

# atributo ptoegido
            self._otro = False



        def prueba(self):
            self.__ganancia

            print(self.__ganancia)    
        
        def mostrar_valor_venta(self):
            return{
                'valor_venta':  (self.precio * self.__ganancia) + self.precio
            }

pitahaya = Producto('pitahaya', 4.50, 100, '2023-02-22')
print(pitahaya.nombre)

print(pitahaya.mostrar_valor_venta())