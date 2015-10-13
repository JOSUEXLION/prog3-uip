#josue de leon
#tarea3

'''
Escriba un programa en Python donde el usuario introduce un numero n y
el programa imprime los primeros n numeros triangulares,
junto con su indice. Los numeros triangulares se originan
de los numeros naturales desde 1 hasta n.
'''

try:
    numero = int(input("Escriba un numero: "))
except ValueError:
    print("Debe ser un numero Natural")
    numero = 0

index = 0
result = 0

if numero < 0:
    print("El numero no es natural")
else:
    while (index <= numero):
        result += index
        index += 1

    print(str(numero) + " - " + str(result))
