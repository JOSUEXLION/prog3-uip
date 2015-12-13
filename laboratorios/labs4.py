#lab4
# Copyright (c) 2015 by Josue de leon. All Rights Reserved.
#grupo con julio Seña

'''
    desarrolle una aplicacion que guarde, en un
    archivo de texto la califaciones de los 5
    quizzes realizados por 3 estudiantes. Cada
    estudiantes tendra su propio archivo de texto
    cuyo nombre de archivo sera igual al nombre del
    estudiante. Ademas debe mostrar en pantalla, el
    valor en promedio de las calificaciones de cada estudiante
    .Utilice todos los conceptos aprendeidos hasta el momento.
'''

def guardarNotas(nombre, notas):
    out_file = open(nombre, "wt")
    for n in notas:
        out_file.write(str(n) + "\n")
    out_file.close()

if __name__ == '__main__':

    ''' /**
     * [allStuden description]
     * @type {Object}
     */'''
    allStudent = {}
    numStudent = 3
    numNote = 5

    i_1 = 0

    while i_1 < numStudent:
        name = input("Nombre del estudiante " + str(i_1 + 1) + " :")
        i_1 += 1
        i_2 = 0
        estudent = allStudent[name] = []
        promedio = 0
        while i_2 < numNote:
            try:
                note = float(input("Escriba su " + str(i_2 + 1) + " nota:"))
            except:
                print("Nota no valida")
            else:
                if (note >= 0 and note <= 100):
                    estudent.append(note)
                    i_2 += 1
                    promedio += note
                else:
                    print("Nota no valida")
        print("promedio: " + str(promedio / 5))

for nombre, notas in allStudent.items():
    guardarNotas(nombre, notas)
print(allStudent
