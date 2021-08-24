def main():
    #escribe tu código abajo de esta línea
    
    print("Saldo de este mes")
    s = float(input("Dame el saldo del mes anterior: "))
    ing = float(input("Dame los ingresos: "))
    egr = float(input("Dame los egresos: "))
    cq = int(input("Dame el número de cheques: "))
    sal = (s+ing)-(egr)-(cq*13)
    por = sal*0.075
    tot = sal-por
    print("El saldo final de la cuenta es:",tot)

    pass

if __name__ == '__main__':
    main()
