class Animal:
    #constructor
    def __init__ (self, nombre:str , raza:str , edad:int, peso:int):
        self.nombre  = nombre
        self.raza = raza 
        self.edad = edad
        self.peso = peso
    #constructor vacío
    def __init__ (self,nombre=None,raza=None, edad=None, peso=None):
        self.nombre  = nombre
        self.raza = raza 
        self.edad = edad
        self.peso = peso
    #getters    
    def get_nombre(self):
        return self.nombre 
    def get_raza(self):
        return self.raza
    def get_edad(self):
        return self.edad
    def get_peso(self):
        return self.peso
    #setters
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_raza(self,raza):
        self.raza = raza
    def set_edad(self,edad):
        self.edad = edad
    def set_peso(self,peso):
        self.peso = peso
        
caballo = Animal ( "Zeus", "pura sangre", 5, 450)
leon = Animal ( "Boulder", "Atlas", 10, 130)
print (caballo.get_edad())