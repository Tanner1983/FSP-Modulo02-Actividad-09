opcion = ""
while opcion != 0:
    print("Venta de bebidas")
    print("[1] Coca cola")
    print("[2] Fanta")
    print("[3] Sprite")
    print("[0] Salida")
    opcion = int(input("Ingrese opcion: "))
    nombreBebida = ""
    
    # valida que los numeros esten dentro del rango 0 al 3
    if opcion < 0 or opcion > 3:
        input("Opción no válida. Presione enter para volver al menú")
        continue
    elif opcion == 0:
        break 

    if opcion == 1:
        nombreBebida = "CocaCola"
    elif opcion == 2:
        nombreBebida = "Fanta"
    elif opcion == 3:
        nombreBebida = "Sprite"

    print("Total de la venta $400, su bebida es: ", nombreBebida)
    input("Presione enter para continuar")    