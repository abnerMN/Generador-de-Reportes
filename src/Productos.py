class Producto:
    def __init__(self, nombre, precio , cantidad):
        self.nombre= nombre
        self.precio=precio
        self.cantidad= cantidad
        self.total=0
    
    def getNombre (self):
        return self.nombre
    
    def getPrecio (self):
        return self.precio
    
    def getCantidad (self):
        return self.cantidad
    
    def setNombre(self, nombre):
        self.nombre= nombre
    
    def setPrecio (self, precio):
        self.precio= precio
    
    def setCantidad (self, cantidad):
        self.cantidad= cantidad

    def calcularTotal(self):
        self.total=self.precio * self.cantidad
    

    
