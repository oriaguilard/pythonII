class Vehiculo:
    #crear un constructor para realizar una instancia de la clase vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    #constructor sin parametros de entrada
    def __init__(self, marca=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto

#creando una instancia de la clase vehiculo
vehiculo_uno = Vehiculo("mazda","blanco","m3",2000,2.5,1.1) #invocar la clase
vehiculo_dos = Vehiculo("bmw","gris","m4",800,2,1.5) 
vehiculo_tres = Vehiculo() 

#accediendo a los atributos del objeto vehiculo
print(vehiculo_uno.marca)
print(vehiculo_uno.color)
print(vehiculo_uno.modelo)
print(vehiculo_uno.peso)
print(vehiculo_uno.ancho)
print(vehiculo_uno.alto)

#cambiar los valores de los atributos del objeto llamado vehiculo_uno
vehiculo_uno.marca = "toyota"
vehiculo_uno.modelo="camry"
vehiculo_uno.color="negro"
vehiculo_uno.peso = 1000
vehiculo_uno.ancho = 2.0
vehiculo_uno.alto= 1.5

print(vehiculo_uno.marca) #toyota