def main():
    #escribe tu código abajo de esta línea
    num=int(input('Dame un número: '))

    par=0
    
    while (num > 0):
        if (num % 2 == 0):
            par=par+1
        else:
            par=par

        num=num//10
    

    print('El número de dígitos pares es: '+ str(int(par)))

    pass

if __name__ == '__main__':
    main()
