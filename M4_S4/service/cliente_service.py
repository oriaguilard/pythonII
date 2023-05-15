from modelo.cliente import Cliente

class ClienteService:
    def crear_cliente(self):
        #(self, nombre, apellido, rut, descuento)
        nombre= input('Ingrese el nombre del cliente: ')
        apellido= input('Ingrese el apellido del cliente: ')
        rut= input('Ingrese el rut del cliente: ')
        descuento= input('Ingrese el descuento= del cliente: ')

        #para crear un cliente se realiza un ainstancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print("cliente creado: ", cliente)