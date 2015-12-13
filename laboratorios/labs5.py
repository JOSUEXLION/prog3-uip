#josue de elon
#lab5
import os
import Hola as c

mensaje = ""

def mostrarMenu():
	print('\n1. Ingresar mensaje')
	print('2. Comparar')
	print('3. Guardar')
	print('4. Mostrar contador')
	print('5. salir')
	print()
		

if __name__ == '__main__': 
	a = c.Hola()
	e = c.Hola()
	opcion_menu = 0
	while True:
		mostrarMenu()
		try:
			opcion_menu = int(input("\nIntroduzca una opcion (1-5): "))
		except:
			print("Opcion no valida")
		else:
			if opcion_menu == 1:
				os.system('cls')
				print("Opcion 1: Ingresar mensaje")
				mensaje = input("\n\nIngrese Mensaje: ")
				a.contar()
			elif opcion_menu == 2:
				os.system('cls')
				if mensaje == "":
					print("POR FAVOR INTRODUZCA UN MENSAJE PRIMERO")
				else:	
					print("Opcion 2: Comparar mensajes\n")
					e.comparar_mensaje(mensaje)
			elif opcion_menu == 3:
				os.system('cls')
				if mensaje == "":
					print("POR FAVOR INTRODUZCA UN MENSAJE PRIMERO")
				else:
					print("Opcion 3: Guardar mensaje")
					e.guardar_mensaje(mensaje)
					print("Mensaje se ha Guardado!")
			elif opcion_menu == 4:
				os.system('cls')
				print("Opcion 4: Mostrar Contador")
				a.mostrar_contador()
			elif opcion_menu == 5:
				break
			else:
				os.system('cls')
				print("Opcion no valida")
				mostrarMenu()
