import os
import math
import cmath
import matplotlib.pyplot as plt

def menu():

    print("Selecciona una opcion")
    print("\t1 - Logaritmo en Base 2")
    print("\t2 - Logartimo en Base 10")
    print("\t3 - Raiz cuadrada de un Numero")
    print("\t4 - Seno de un Angulo")
    print("\t5 - Coseno de un Angulo")
    print("\t6 - Raiz de un Numero Complejo")
    print("\t7 - Conversion a polar")
    print("\t8 - Suma de dos numeros complejos")
    print("\t9 - Multiplicacion de dos numeros complejos")
    print("\t10 - ")
    print("\t11 - ")
    print("\t12 - ")
    print("\t13 - ")
    print("\t14 - ")
    print("\t15 - ")
    print("\t16 - Salir")

while True:

    menu()

    opcionMenu = input("Seleccione una opcion")

    if opcionMenu == "1":

        print("Operaciones con Log Base 2")
        x = int(input("Ingrese un numero:"))
        log=math.log2(x)
        print("El logaritmo en Base 2 de:" , x , "es igual a:" , log)

    elif opcionMenu == "2":

        print("Operaciones con Log Base 10")
        x=int(input("Ingrese un numero:"))
        log10=math.log10(x)
        print("El logaritmo en Base 10 de:" , x, "es igual a:", log10)

    elif opcionMenu == "3":

        print("Raiz Cuadrada de un Numero")
        x=int(input("Ingrese un numero:"))
        sqrt=math.sqrt(x)
        print("Raiz cuadrada de:" , x, "es igual a:" , sqrt)

    elif opcionMenu == "4":

        print("Seno de un Angulo")
        x=int(input("Ingrese el valor del angulo:"))
        sin=math.sin(x)
        print("El seno del angulo:",x, "es igual a:", sin)

    elif opcionMenu == "5":

        print("Coseno de un Angulo")
        x=int(input("Ingrese el valor del angulo:"))
        cos=math.cos(x)
        print("El coseno del angulo:",x,"es igual a:",cos)

    elif opcionMenu == "6":

        print("Raiz de un Numero Complejo negativo")
        x=int(input("Ingrese un valor negativo:"))
        sqrt=cmath.sqrt(x)
        print("La raiz negativa es igual a:",sqrt)

    elif opcionMenu == "7":

        print("Convertir a polar")
        x=int(input("Ingrese la parte real de un numero complejo:"))
        y=int(input("Ingrese la parte imaginaria de un numero complejo:"))
        c=complex(x,y)
        print(c)
        polar=cmath.polar(c)
        print("El numero:",c,"en coordenadas polares es igual a:",polar)

    elif opcionMenu == "8":

        print("Suma de dos numeros complejos")
        x1 = int(input("Ingrese la parte real del primer numero complejo:"))
        y1 = int(input("Ingrese la parte imaginaria del primer numero complejo:"))
        c1=complex(x1,y1)
        print(c1)

        x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
        y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
        c2 = complex(x2, y2)
        print(c2)

        sum=c1+c2

        print("La suma de los numeros:",c1,c2,"es igual a:" ,sum)

    elif opcionMenu == "9":

        print("Suma de dos numeros complejos")
        x1 = int(input("Ingrese la parte real del primer numero complejo:"))
        y1 = int(input("Ingrese la parte imaginaria del primer numero complejo:"))
        c1 = complex(x1, y1)
        print(c1)

        x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
        y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
        c2 = complex(x2, y2)
        print(c2)

        mult = c1 * c2

        print("La multiplicacion de los numeros:", c1, c2, "es igual a:", mult)

    elif opcionMenu== "10":

        lista=(1,2,3,4,5)
        plt.plot(lista)



    elif opcionMenu == "16":

        exit()