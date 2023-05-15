from modelo.persona import Persona

class Supervisor (Persona):
    def __init__(self, nombre, apellido, rut, area):
        super().__init__(nombre, apellido, rut) #invocando a los atributos de la super clases
        self._area = area
        
    @property #get
    def area (self):
        return self._area

    @area.setter #set
    def area (self,area):
        self._area = area
        
    #funcion para imprimir el obj string 
    def __str_(self):
        return f'Supervisor ( nombre = {self._nombre}, apellido= {self._apellido}, rut = {self._rut}, area={self._area})'
    