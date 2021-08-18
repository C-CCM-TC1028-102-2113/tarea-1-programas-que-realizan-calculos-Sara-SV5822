def main():
    #escribe tu código abajo de esta línea

    harina=float(input('Dame la harina en gramos: '))

    levadura= float(((harina/1000)*50)/1)

    print('Necesitas estos gramos de levadura: '+ str(levadura))

    pass

if __name__ == '__main__':
    main()


