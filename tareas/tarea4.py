#josue de leon
#tarea4
'''
intrucciones
1. Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos
correspondientes.

'''
minuts = int(input("Escriba el tiempo en minutos: "))

dias = int(minuts / 1440)
minutos = minuts % 1440
horas = int(minuts / 60)
minutos = minuts % 60

print('Dias: ' + str(dias) + ', Horas: ' + str(horas) + ', Minutos: ' + str(minuts)+'\ncorrespondientes')
 
