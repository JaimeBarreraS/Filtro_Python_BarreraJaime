import json
from colorama import Fore, Style

def cargar():
     with open("Movistar.json", 'r' ) as f:
        Movistar=json.load(f)


def guardar(Movistar):
    with open("Movistar.json", 'w') as f:
        json.dump(Movistar,f) 


while True: 
    print(Fore.GREEN + "=== MENU MOVISTAR ====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Crear Usuarios" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Usuarios" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Personalización de Servicios" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Gestión de la Fidelización de Clientes" + Style.RESET_ALL)
    print(Fore.RED + "0. Salir" + Style.RESET_ALL) 
    print("")
    opcion=int(input("Selecciona una opcion: "))

    if opcion==0: #Salir del programa
        print(Fore.BLACK + "Gracias por utilizar" + Style.RESET_ALL)
        break


    elif opcion==1: # Registro y Gestion de Usuarios
        print(Fore.GREEN + "---- CREAR USUARIO ----" + Style.RESET_ALL)
        Movistar={ 
            "usuario":{
                "nombres": input("Ingresa los nombres del Usuario: "),
                "apellido": input("Ingresa los apellido del Usuario: "),
                "# de Identificacion": int(input("Ingresa la CC del usuario: ")),
                "direccion": input("Ingresa Direccion del Usuario: "),
                "Celular": int(input("Ingresa el numero de Celular: ")),
                "tipo de cliente": input("Ingresa el tipo de usuario (nuevo, regular, leal: ")
                }
        }
        guardar(Movistar)
        input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)
    
    elif opcion==2: #Mostrar usuarios
        print(Fore.GREEN + "---- mostrar usuarios nuevos ----" + Style.RESET_ALL)
        for i in i:
            print(f"Usuarios nuevos {Movistar['usuario']}")

        print(Fore.GREEN + "---- mostrar usuarios regulares ----" + Style.RESET_ALL)
        for i in i:
            print(f"Usuarios nuevos {Movistar['usuario']}")
        
        print(Fore.GREEN + "---- mostrar usuarios leal ----" + Style.RESET_ALL)
        for i in i: 
            print(f"Usuarios nuevos {Movistar['usuario']}")

        input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)

    elif opcion==3: #personalizar servicios 
        print(Fore.GREEN + "---- SERVICIOS PERSONALIZADOS ----" + Style.RESET_ALL)
        Movistar={ 
            "usuario":{
                "tipo de cliente": input("Ingresa el tipo de usuario (nuevo, regular, leal: "),
                "internet": input("Eliga la instlacion de tu internet (Satelital, Fibra optica): "),
                "megas": input("megas para le internet  (10 megas, 60 megas, 80 megas, +120 megas: "),
                "Television": input("Eliga la instlacion de tv (Satelital, Fibra optica): "),
                "Plan de tv": input("Elige plan de tv (120 canales, 200 canales, +400 canales): ")
                }
        }

        guardar(Movistar)
        input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)

    elif opcion==4: #Fidelización de clientes
        print(Fore.GREEN + "==== BONIFICACION ====" + Style.RESET_ALL)
        print(Fore.YELLOW + "---- mostrar usuarios leal ----" + Style.RESET_ALL)
        cargar()
        Movistar['usuario']
        Movistar: {
             'usuario':{
                 "bonificacion de fidelidad": bonificacion,
        }} # type: ignore

        for i in i: 
                print(f"Usuarios nuevos {Movistar['usuario']}")

        print(Fore.BLUE + "---- Bonificacion del 70% ----" + Style.RESET_ALL)
        
        for i in Movistar('usuario'):
                bonificacion= 0.10 - 0.70 
                Movistar['usuario', bonificacion]

    guardar(Movistar)
    input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)

# Hecho por Jaime Barrera Sandoval CC 1093925253
