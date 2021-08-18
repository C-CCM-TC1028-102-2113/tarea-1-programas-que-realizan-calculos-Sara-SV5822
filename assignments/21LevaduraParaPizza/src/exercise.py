def main():
    #escribe tu código abajo de esta línea

    harina=float(input('Dame la harina en gramos: '))

    kg= harina/1000
    levadura= kg*50/1

    print('Necesitas estos gramos de levadura: '+ str(levadura))

    pass

if __name__ == '__main__':
    main()

