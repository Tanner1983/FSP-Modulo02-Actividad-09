opcion = ""
while opcion != 0:
    print("Venta de bebidas")
    print("[1] Estreno")
    print("[2] 3D")
    print("[0] Salida")
    opcion = int(input("Ingrese opcion: "))
    if opcion ==1:
        entradas=input("Ingrese cantidad de entradas: ")
        print("Pelicula de estreno - Valor de entrada 4200 - total a pagar :$",int(entradas)*4200)
        input("\nPresione tecla para continuar......")
    elif opcion ==2:
        entradas=input("Ingrese cantidad de entradas: ")
        print("Pelicula de estreno - Valor de entrada 5500 - total a pagar :$",int(entradas)*5500)
        input("\nPresione tecla para continuar......")
    elif opcion == 0:
        break
    else:
        print("Opcion invalida")
        input("Presione una tecla para continuar......")