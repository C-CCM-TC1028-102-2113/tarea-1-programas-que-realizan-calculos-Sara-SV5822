def main():
    #escribe tu código abajo de esta línea

    time= float(input('Dame los minutos: '))

    cen= float((5.7*60/10)*time)

    print('Centímetros recorridos: '+ str(round(float(cen),1)))

    pass

if __name__ == '__main__':
    main()
