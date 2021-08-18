def main():
    #escribe tu código abajo de esta línea
    saldo_a=float(input('Dame el saldo del mes anterior: '))
    ingresos= float(input('Dame los ingresos: '))
    egresos= float(input('Dame los egresos: '))
    num=int(input('Dame el número de cheques: '))

    saldo_f= saldo_a-egresos+ingresos
    total= saldo_f-(saldo_f*0.075)-(num*13)

    print('El saldo final de la cuenta es: '+ str(total))

    pass

if __name__ == '__main__':
    main()
