#Tarea 5 
#josue de leon
'''Elaborar un programa en Python que encueste a 10 personas y las clasifique seg˙n el deporte que practica. 
La lista de deportes v·lidos son: Ajedrez, Atletismo, Baloncesto, F˙tbol, Karate, NataciÛn, Volleyball,
Flag y Ping Pong. Puede darse el caso que no le guste ninguno de los deportes anteriores. 
Si es asÌ, entonces se puede seleccionar la opciÛn Otros. Al final el programa debe mostrar estadÌsticas de la encuesta
e indicar cu·l es el deporte con mayor preferencia de los encuestados.'''

import os
j=0
aje=0
atle=0
bal=0
fut=0
kar=0
nat=0
voll=0
fla=0
pin=0
otro=0

def mostrarMenu():
	print('\n1. Ajedrez')
	print('2. Atletismo')
	print('3. Baloncesto')
	print('4. Futbol')
	print('5. Karate')
	print('6. Natacion')
	print('7. Volleyball')
	print('8. Flag')
	print('9. Ping Pong')
	print('10. Otros')
	print()

for i in range (0, 10):
	os.system('cls')
	j= (j+1)
	mostrarMenu()
	print("Persona #"+str(j))
	opc = int(input("\nElija una opcion: "))
	if opc == 1:
		aje= (aje+1)
	elif opc == 2:
		atle= (atle+1)
	elif opc == 3:
		bal= (bal+1)
	elif opc ==4:
		fut= (fut+1)
	elif opc ==5:
		kar= (kar+1)
	elif opc ==6:
		nat=(nat+1)
	if opc == 7:
		voll= (voll+1)
	elif opc == 8:
		fla= (fla+1)
	elif opc == 9:
		pin= (pin+1)
	elif opc ==10:
		otro= (otro+1)
	elif (opc<1) or (opc>10):
		print('introduzca numero entre las opciones')
		input()

os.system('cls')
print("PORCENTAJES:")
print("1.Ajedrez:    ",   str((aje/10)*100)+"%")
print("2.Atletismo:  ", str((atle/10)*100)+"%")
print("3.Baloncesto: ",str((bal/10)*100)+"%")
print("4.Futbol:     ",    str((fut/10)*100)+"%")
print("5.Karate:     ",    str((kar/10)*100)+"%")
print("6.Natacion:   ",  str((nat/10)*100)+"%")
print("7.Volleyball: ",str((voll/10)*100)+"%")		
print("8.Flag:       ",      str((fla/10)*100)+"%")		
print("9.Pin Pong:   ",  str((pin/10)*100)+"%")
print("10.Otros:     ",   str((otro/10)*100)+"%")
