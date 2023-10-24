""" ------------------------  TUPLAS   ---------------------------

1- las tuplas son inmutables.
2- no se pueden modificar en su contenido.
3- Contienen distintos tipos de datos
4- si se requiere añadir algo a una tupla se tiene que convertir primero a una lista y cuando se haya hecho la conversion 
se puede modificar
5- se puede acceder a la tupla indicando el indice de la misma y comienza desde Cero
6- si se requiere recorrer la tupla usamos el ciclo for
7- se puede hacer Join en las Tuplas, es decir unir Tuplas
8- para conocer el tamaño usamos la funcion = len(dias_semana)
9- las tuplas permiten duplicar valores"""


#----------- TUPLAS ------------------

dias_semana = ("Lunes" , "Martes" , "Miercoles", "Jueves" , "Viernes" , "Sabado" , "Domingo" )
print(type(dias_semana))

print("--------------------------------------------------------------")
#----------------------------------------------------------------------

#Funcion Len
print(len(dias_semana))

print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])


print("--------------------------------------------------------------")
#----------------------------------------------------------------------

#Podemos hacer Slicing indicando el rango que queremos Imprimir

print(dias_semana[:7])
print(dias_semana[0:])
print(dias_semana[-1])
print(dias_semana[:-1])
print(dias_semana[2:5])


print("--------------------------------------------------------------")
#----------------------------------------------------------------------

#Para Recorrer las Tuplas usamos for para iterar por los indices

for i in range(len(dias_semana)):
    print(dias_semana[i])


print("--------------------------------------------------------------")
#----------------------------------------------------------------------

# Convertir la Tupla en LIsta =  Para cambiar algun valor de la Tupla o añadir primero debemos convertirla a una lista

dias_semana_lista = list(dias_semana)
print(type(dias_semana_lista))

dias_semana_lista.append("Festivo") # append = añade al final un objeto
print(dias_semana_lista[:8])


dias_semana_lista.pop() # pop = elimina el ultimo objeto
print(dias_semana_lista)

print("--------------------------------------------------------------")
#----------------------------------------------------------------------

# Convertir la Lista en Tupla

dias_semana_lista = tuple(dias_semana)
print(type(dias_semana))

