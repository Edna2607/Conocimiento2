"""----------------------   CONJUNTOS -----------------------

1- los conjuntos son (inmutables) - no son del todo inmutables ya que el conjunto se deja añadir
2- son desordenados = es decir que cuando se llama no se tiene certeza el orden en que los mostrará
3- no son indexados
4- NO permite duplicados en cuanto a los valores"""

#CONJUNTO
vocales = {"a", "e" , "i" , "o", "u"}
print(type(vocales))
print(len(vocales))


print("--------------------------------------------------------------")
#----------------------------------------------------------------------

# Para Recorrer los conjuntos se usa = in

for i in vocales:
    print(vocales) 

print("--------------------")
for i in vocales:
    print(vocales) 

print("--------------------")
for i in vocales:
    print(vocales) 


print("--------------------------------------------------------------")
#----------------------------------------------------------------------

# Tienen el metodo add y tienen el metodo remove

# Añadir

vocales.add("@")

for i in vocales:
    print(vocales) 

    
print("--------------------------------------------------------------")
#----------------------------------------------------------------------

# Remover
vocales.remove("@")

for i in vocales:
    print(vocales) 

print("--------------------------------------------------------------")
#----------------------------------------------------------------------