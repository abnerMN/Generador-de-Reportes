from Productos import Producto

class Periodo:
    def __init__ (self, month, year):
        self.month= month
        self.year= year
        self.productos=[]
    
    def agregarProducto (self, nombre, precio, cantidad):
        aux= Producto (nombre, precio, cantidad)
    
