def main():
    #escribe tu código abajo de esta línea

    time=round(float(input('Dame los minutos: ')),1)

    vel=5.7/10*60

    dis=round(vel*time,1)

    print('Centímetros recorridos: '+ str(dis))

    pass

if __name__ == '__main__':
    main()
