
def calcular(num, numPrimo):

    contador = 0
    numPrimo = False

    for i in range(1, num + 1):
        if (num % i) == 0:
            contador = contador + 1
        if contador >= 3:
            numPrimo = True
            break

    if contador == 2 or numPrimo == False:
        print("El numero ingresado es primo")

    else:
        print("El numero ingresado no es primo")

    return numPrimo


def main():

    contador = 0
    numPrimo = False

    num=int(input("Ingrese un numero entero: "))

    calcular(num, numPrimo)

if __name__ == '__main__':
    main()

