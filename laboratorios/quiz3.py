""""dado el intervalo de tiempo en segundos, 
calcular los segundos restantes 
que corresponden para convertirse exactamente en minutos. 
este programa debe funcionarar 5 oportunidades
"""

repeti = []

numRep = 5

apple = 0
while apple < numRep:
    apple += 1

    melon = input("Ingese numero en segundos para el  "+str(apple)+" intento : ")

    repeti.append(float(melon))

grape = 0
for tiempo in repeti:
    grape+= 1
    restante= tiempo % 60
    pear= 60 - restante
    print("Para " + str(grape) + " los segundos restantes son: " + str(pear))
	

