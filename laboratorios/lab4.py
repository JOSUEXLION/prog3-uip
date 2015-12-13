#lab 4
#josue dde leon


for i in range (1, 4):
	nombre = input("\n\nintroduce nombre: ")
	n1 = input ("Introduce nota 1: ")
	n2 = input ("Introduce nota 2: ")
	n3 = input ("Introduce nota 3: ")
	n4 = input ("Introduce nota 4: ")
	n5 = input ("Introduce nota 5: ")
	prom=(float(n1)+float(n2)+float(n3)+float(n4)+float(n5))/5	
	print ("\nNombre: " + str(nombre))
	print ("\nQuiz 1: " + str(n1))
	print ("Quiz 2: " + str(n2))
	print ("Quiz 3: " + str(n3))
	print ("Quiz 4: " + str(n4))
	print ("Quiz 5: " + str(n5))
	print ("\n\nEl promedio de " + str(nombre) + " es " + str(prom))
	archivo = open(nombre, 'w')
	archivo.write("Nombre: " + str(nombre))
	archivo.write("\nquiz 1: " + n1)
	archivo.write("\nquiz 2: " + n2)
	archivo.write("\nquiz 3: " + n3)
	archivo.write("\nquiz 4: " + n4)
	archivo.write("\nquiz 5: " + n5)
	archivo.write("\nEl promedio de " + str(nombre) + " es " + str(prom))
	archivo.close() 
