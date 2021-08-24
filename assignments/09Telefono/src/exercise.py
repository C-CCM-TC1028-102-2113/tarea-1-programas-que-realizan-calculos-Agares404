def main():
    #escribe tu código abajo de esta línea

    print("Costo mensual del teléfono")
    men = int(input("Dame el número de mensajes: "))
    me = float(input("Dame el numero de megas: "))
    min = int(input("Dame el número de minutos: "))
    tot = (men+me+min)*.8
    print("El costo mensual es: ",tot)

    #Leer los datos
    pass


if __name__ == '__main__':
    main()
