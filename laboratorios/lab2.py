'''
El empleador esta celebrando aniversario y ofrecera a sus clientes una serie
de ofertas que se traduciran en incremeno de sus ventas. Las reglas de la
ofertas se basan en un porcentaje de descuento sobre el total de compra, que
estarian variando dependiendo del monto adquirido:
por un monto mayor o igual a $500 descuento de 30%
por un monto menor de $500 y mayor que 200 descuento de 20%
por un monto menor de $200 -> y mayor o igual a $100 descuento de10%
'''
#lab2
#josue de leon
contador = 1
tot = 0
des= 0
while contador <= 5:
	print ("Cliente "+str(contador))
	nombre = input("Introduzca nombre del cliente: ")
	mont = input("Introduzca monto: ")
	if float (mont) < 200 and float (mont) >= 100:
		des= 0.10
		tot= float(mont) - (float (mont)*des)
		print("El total de su compra es: "+ str(tot))
	elif float (mont) < 500 and float (mont) >= 200:
		des= 0.20
		tot= float(mont) - (float (mont)*des)
		print("El total de su compra es: "+ str(tot))
	elif float (mont) >= 500:
		des= 0.30
		tot= float(mont) - (float (mont)*des)
		print("El total de su compra es: "+ str(tot))
		
	contador = contador + 1
print ("End")
