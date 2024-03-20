from time import sleep

hora = minuto = segundo = 0
print('Pressione ENTER tecla para CRONOMETRAR\n')

while True:
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
    print('Hora: {}, Minutos: {}, Segundos: {}' .format(hora, minuto, segundo))
    sleep(1)