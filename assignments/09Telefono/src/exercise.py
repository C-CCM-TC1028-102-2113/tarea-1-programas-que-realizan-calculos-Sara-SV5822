def main():
    #escribe tu código abajo de esta línea

    msj=int(input('Dame el número de mensajes: '))
    megas=float(input('Dame el número de megas: '))
    min=int(input('Dame el número de minutos: '))

    costo=(msj+megas+min)*0.80

    print('El costo mensual es: '+ str(costo))

    pass

if __name__ == '__main__':
    main()
