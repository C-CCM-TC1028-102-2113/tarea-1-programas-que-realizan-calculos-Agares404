def main():
    #escribe tu código abajo de esta línea

    print("Compra de videojuegos")
    n = int(input("Dame la cantidad de juegos nuevos: "))
    v = int(input("Dame la cantidad de juegos viejos: "))
    tot = (n*1000)+(v*350)
    print("El total de compra es: ",tot)

   pass



if __name__ == '__main__':
    main()
