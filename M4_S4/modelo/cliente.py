from modelo.persona import Persona

class Cliente (Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut) #invocando a los atributos de la super clases
        self._descuento = descuento
        
    @property #get
    def descuento (self):
        return self._descuento

    @descuento.setter #set
    def descuento (self,descuento):
        self._descuento = descuento
        
    #funcion para imprimir el obj string 
    def __str__(self):
        return f'Cliente ( nombre = {self._nombre}, apellido= {self._apellido}, rut = {self._rut}, descuento={self._descuento})'
    