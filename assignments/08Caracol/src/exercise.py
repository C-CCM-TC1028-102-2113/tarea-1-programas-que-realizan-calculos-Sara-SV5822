def main():
  #escribe tu código abajo de esta línea
  min=float(input('Dame los minutos: '))

  cm=round(float(min*0.57*60),1)

  print('Centímetros recorridos: '+ str(cm))

if __name__ == '__main__':
    main()
