import random
import os

contador=0;numeros=0

print("Ingrese la cantidad de sorteos a realizar")
cantidad_sorteos=int(input(": "))

while contador < cantidad_sorteos:
    numeros=0
    print("Sorteo n°", contador+1)
    while numeros < 15:
        print("El numero sorteado es: ", random.randint(1, 99))
        numeros+=1
        input("Presione una tecla para continuar.....")
    contador+=1    
    print("\n==============Sorteo N°",contador,"Finalizado ==========\n=============================================== ")
    input("Presione una tecla para continuar.....")
    os.system("cls")
    