"""LAS LISTAS
*son estructuras de datos lineales
*se crean usando [] 
*las listas son ordenadas (Orden de insersión), esto quiere decir que el ultimo dato ingresado ocupara la ultima posicion.
*Emplea metodos para manipular los Items de la misma.
*Como los arrays la primera posicion inicia en 0
*Permite items duplicados.
*las listas son mutables, es decir podemos agregar, actualizar o remover items
*Puede contener distintos tipos de datos
"""

nombres = ["Juan", "Pepito", "Maria", "Lisa"]

#El metodo len() nos permite validar el tamaño de la lista.
print(len(nombres))
print(type(nombres))

#---------------------------------------------------------

listaDatos = ["Pepito","Perez",1000100100, 1.80, True]

print(listaDatos[2])
print(f"El numero de documento es: {listaDatos[2]}")

#Slicing de datos : De esta forma me imprime desde un numero : hasta otro numero, menos la ultima posicion

#------------------------------------------------------
#CONSULTA DE LAS LISTAS CON NUMEROS POSITIVOS
print(listaDatos[0:2])
print(listaDatos[1:4])

#Imprime todos menos el ultimo 
print(listaDatos[:4])

#Imprime desde la segunda posicion hasta el ultimo dato
print(listaDatos[2:])

#Ignora los extremos con numeros positivos
print(listaDatos[1:4])

#------------------------------------------------------
#CONSULTA DE LAS LISTAS CON NUMEROS NEGATIVOS
#Hace la consulta desde atras hacia adelante
print(listaDatos[:-4])

#Ignora los extremos con numeros negativos
print(listaDatos[-4:-1])
#------------------------------------------------------

