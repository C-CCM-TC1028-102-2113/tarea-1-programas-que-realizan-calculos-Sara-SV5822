def main():
    #escribe tu código abajo de esta línea
    saldo_a=float(input('Dame el saldo del mes anterior: '))
    ingresos= float(input('Dame los ingresos: '))
    egresos= float(input('Dame los egresos: '))
    num=int(input('Dame el número de cheques: '))

    saldo_f= saldo_a-egresos+ingresos-(num*13)
    total= saldo_f*(100-7.5)/100

    print('El saldo final de la cuenta es: '+ str(total))

    pass

if __name__ == '__main__':
    main()
