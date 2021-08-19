def main():
    #escribe tu código abajo de esta línea
    vel = 5.7 
    min = float(input('Dame los minutos: '))
    
    cm = vel/10
    time = min*60
    
    total = cm * time
    print('Centímetros recorridos: '+ str(round(total,1)))

    pass

if __name__ == '__main__':
    main()
