def main():
    #escribe tu código abajo de esta línea
    saldo_a=round(float(input('Dame el saldo del mes anterior: ')),1)
    ingresos= round(float(input('Dame los ingresos: ')),2)
    egresos= round(float(input('Dame los egresos: ')),2)
    num=int(input('Dame el número de cheques: '))

    saldo_f= saldo_a-egresos+ingresos-(num*13)
    total= saldo_f*(92.5)/100

    print('El saldo final de la cuenta es: '+ str(total))

    pass

if __name__ == '__main__':
    main()
