def main():
    #escribe tu código abajo de esta línea
    time=float(input('Dame los minutos: '))

    vel=5.7
    dist=float((vel*6)*time)

    print('Centímetros recorridos: '+ str(round(dist,1)))



    pass

if __name__ == '__main__':
    main()
