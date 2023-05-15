class Persona:
    
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._rut = rut
        
    @property #get
    def nombre (self):
        return self._nombre

    @nombre.setter #set
    def nombre (self,nombre):
        self._nombre = nombre

    @property #get
    def apellido (self):
        return self._apellido

    @apellido.setter #set
    def apellido (self,apellido):
        self._apellido = apellido

    @property #get
    def rut (self):
        return self._rut

    @rut.setter #set
    def rut (self,rut):
        self._rut = rut
    
    #funcion o metodo    
    def get_tipo(self):
        print(f'soy del tipo {self}')
        print(type(self))
    #funcion para imprimir el obj string 
    def __str__(self):
        return f'Persona ( nombre = {self._nombre}, apellido= {self._apellido}, rut = {self._rut})'
    