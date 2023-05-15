from modelo.persona import Persona
from modelo.cliente import Cliente
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService

def main():
    #creando instancias para acceder a una clase
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()
    
    while True:
        menu_service.imprimir_menu() #imprimiendo menu
        opcion = input ("ingrese una opción: ")        
        match opcion:
            case "1":
                cliente_service.crear_cliente()
            case "2":
                supervisor_service.crear_supervisor()
            case "3":
                print("saliendo del programa")
                break
            case _:
                print("opcion invalida")
if __name__ == "__main__": #funcion inicializadora si el nombre es main, iniciar el main
    main()

"""
persona = Persona ("orianna", "aguilar","13321")
print(persona)
print(str(persona))
persona.get_tipo()
cliente = Cliente ("adrian", "aaaaa","11312","40%")
print(cliente)
print(str(cliente))
cliente.get_tipo()
"""