class Vehiculo:
    #constructor con parametros para realizar una instancia de la clase Vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0
        self.encendido = False
        
#getters and setters son funciones para obtener o dar valor a los atributos
#getter
    def get_marca(self):
        return self.marca

    def get_color(self):
        return self.color

    def get_modelo(self):
        return self.modelo
    
    def get_peso(self):
        return self.peso

    def get_ancho(self):
        return self.ancho
    
    def get_alto(self):
        return self.alto
    
    def get_velocidad(self):
        return self.velocidad
    
    def get_encendido(self):
        return self.encendido
#setter    
    def set_marca(self, marca): #nunca se puede cmbiar el nombre de un atributo
        self.marca = marca

    def set_color(self, color):
        self.color = color

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_peso(self, peso):
        self.peso = peso
        
    def set_ancho(self, ancho):
        self.ancho = ancho
        
    def set_alto(self, alto):
        self.alto = alto
        
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    
    def set_encendido(self, encendido):
        self.encendido = encendido       
            
#funciones que realiza el objeto accediendo a traves de la instancia
    def arrancar(self):
        if not self.encendido:
            self.encendido = True #se cambia a true para cambiar el estado del vehiculo
            self.velocidad = 10
            return f"vehiculo de marca {self.marca} esta en encendido"
        else:
            return f"vehiculo de marca {self.marca} ya se encuentra en encendido"

    def frenar(self):
        if self.velocidad and self.velocidad > 0:
            self.velocidad -= 10
            return f"vehiculo de marca {self.marca} y {self.modelo} se ha detenido"
        else:
            return f"vehiculo de marca {self.marca} y {self.modelo} ya esta detenido"

    def girar_izq(self):
        if self.encendido:
            return f"vehiculo de marca {self.marca} esta girando a la izquierda"
        else:
            return f"vehiculo de marca {self.marca} debe estar en encendido"

    def girar_der(self):
        if self.encendido:
            return f"vehiculo de marca {self.marca} esta girando a la derecha"
        else:
            return f"vehiculo de marca {self.marca} debe estar en encendido"

    def apagar (self):
        if self.encendido:
            self.encendido = False
            return f"vehiculo de marca {self.marca} se ha apagado"
        else:
            return f"vehiculo de marca {self.marca} ya esta apagado"

    def encender (self):
        if not self.encendido:
            self.encendido = True
            return f"vehiculo de marca {self.marca} se ha encendido"
        else:
            return f"vehiculo de marca {self.marca} ya esta encendido"

    def acelerar ( self):
        if self.encendido:
            self.velocidad +=10
            return f"vehiculo de marca {self.marca} ha aumentado su velocidad {self.velocidad}"
        else:
            return f"vehiculo de marca {self.marca} no aumenta su velocidad por que est aapagado"

    def retroceder(self):
        if self.encendido:
            self.velocidad -=10
            return f"vehiculo de marca {self.marca} ha disminuido su velocidad en {self.velocidad} y esta retrocediendo"
        else:
            return f"vehiculo de marca {self.marca} no puede retroceder, no  esta encendido"        

#instanciar vechiculos para realizar las acciones mediante sus funciones o metodos
mazda = Vehiculo ("mazda", "blanco", "m4", 2000,2.5,2)
toyota = Vehiculo ("toyota", "negro", "s1", 1000,1.5,1)

#cambiar el comportamiento mediante las funciones, accediendo desde la instancia a las funciones

print(mazda.arrancar())
print(mazda.acelerar())
print(mazda.encender())
print(mazda.apagar())
print("-----------------")
print(toyota.encender())
print(toyota.encender())
print(toyota.arrancar())
print(toyota.acelerar())
print(toyota.frenar())

#get/obtener el valor del atributo a traves de notacion de puntos
print(mazda.color) #opcion 1
print(mazda.get_color()) #opcion 2

#setear/cambiar un valor del atributo a traves de notacion de puntos
mazda.color = "Azul"
mazda.set_color("Rosado")
print(mazda.get_color())