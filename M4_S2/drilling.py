class Persona:
    def __init__(self, nombre, apellido, genero, edad , estatura, peso):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    @property  #get
    def nombre(self):
        return self._nombre
    @nombre.setter #set
    def nombre(self,nombre):
        self._nombre = nombre

    @property  #get
    def apellido(self):
        return self._apellido
    @apellido.setter #set
    def apellido(self,apellido):
        self._apellido = apellido

    @property  #get
    def genero(self):
        return self._genero
    @genero.setter #set
    def genero(self,genero):
        self._genero = genero

    @property  #get
    def edad(self):
        return self._edad
    @edad.setter #set
    def edad(self,edad):
        self._edad = edad

    @property  #get
    def estatura(self):
        return self._estatura
    @estatura.setter #set
    def estatura(self,estatura):
        self._estatura = estatura

    @property  #get
    def peso(self):
        return self._peso
    @peso.setter #set
    def peso(self,peso):
        self._peso = peso

    def __str__(self) :
        return f'Persona(nombre={self._nombre}, apellido={self._apellido}, genero={self._genero}, edad={self._edad} , estatura={self._estatura}, peso={self._peso})'


persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78 , 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

print (f'el nombre de persona1 es {persona_1.nombre} y su apellido es {persona_1.apellido}')

print(persona_1)
persona_1.nombre = "David"

print(persona_1.edad)
persona_1.edad= 21
print(persona_1.edad)
print("_____________")

print(persona_2)
print(persona_2.apellido)
persona_2.apellido= "duran"
print(persona_2.apellido)


