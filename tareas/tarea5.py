#josue de leon 
#lista de supermercado

#una tupla para las opciones, y una lista para la lista
import os
lista = []
opciones = ("1. Añadir producto a la lista.","2. Borrar el ultimo producto de la lista.","3. Mostrar toda la lista.")
control = 1
print("\n\n\tBienvenido a su lista de compras.\n\nRecuerde que su lista esta en blanco, asi que lo primero que debe hacer es\nagregar nuevos elementos.")
while control == 1:
	print("\nSeleccione que desea hacer:\n\n\t"+str(opciones[0])+"\n\t"+str(opciones[1])+"\n\t"+str(opciones[2])+"\n")
	seleccion = int(input("Escoja una opcion: "))
	if seleccion == 1:
		print('*Ingrese un producto para añadir a su lista.\n*Ingrese "fin" para finalizar su lista.')
		producto_lista = ''
		while producto_lista.lower() != "fin": 
			producto_lista = input()
			if producto_lista.lower() != "fin":
				lista.append(producto_lista)	
	elif seleccion == 2:
		del lista[(len(lista)-1)]
		print("El ultimo elemento ha sido borrado!")
	elif seleccion == 3:
		centinela = 1
		while centinela <= len(lista):
			print("- "+lista[centinela-1])
			centinela = centinela + 1
	control = int(input('\n¿Desea continuar con su lista?\n- Presione "1" para CONTINUAR.\n- Si desea SALIR presione "0": '))
	os.system("cls")
