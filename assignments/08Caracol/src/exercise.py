def main():
    #escribe tu código abajo de esta línea

    time=float(input('Dame los minutos: '))

    vel=5.7/10*60

    dis=round(vel*time,1)

    print('Centímetros recorridos: '+ str(dis))

    pass

if __name__ == '__main__':
    main()
