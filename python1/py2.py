import os


def menu():
    os.system('clear')
    print("Selecciona una opcion")
    print("\t1 - Logaritmo en base 2")
    print("\t2 - Salir")


while True:

    menu()

        opcionMenu = input("Seleccione una opcion")

        if opcionMenu == "1":

            x = int(input("Ingrese un numero:"))


        elif opcionMenu == "2":

            exit()