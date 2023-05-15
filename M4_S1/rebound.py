class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def comer (self):
        print(f"el animal con nombre {self.nombre} esta comiendo")
        
    def caminar(self):
        print(f"el animal de raza {self.raza} kilos esta caminando")
        
    def dormir(self):
        print(f"el animal de edad {self.edad} años esta durmiendo")
        
#definir una estancia de tipo animal para un objeto

#perro
perro = Animal("brando", "san bernardo", 3, 30 )

#gato
gato = Animal("roll", "persa", 4, 3 )

#setear valores a los atributos
perro.nombre = "bob"


perro.caminar()
perro.comer()
perro.dormir()