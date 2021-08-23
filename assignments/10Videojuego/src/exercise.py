def main():
    #escribe tu código abajo de esta línea
    juego_1=int(input('Dame la cantidad de juegos nuevos: '))
    juego_2=int(input('Dame la cantidad de juegos usados: '))

    total=(juego_1*1000)+(juego_2*350)

    print('El total de la compra es: '+ str(total))

    pass

if __name__ == '__main__':
    main()
