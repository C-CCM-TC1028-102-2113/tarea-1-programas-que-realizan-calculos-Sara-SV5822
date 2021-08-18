def main():
    #escribe tu código abajo de esta línea
    pag=int(input('Dame el número de palabras: '))

    if ((pag % 475) == 0):
        pag=pag/475
        costo= float((pag*60)*.9)
        print('El costo de la publicación es: '+ str(costo))
    


    else:
        pag= (pag//475)+1
        costo= float((pag*60)*.9)
        print('El costo de la publicación es: '+ str(costo))

    pass

if __name__ == '__main__':
    main()
