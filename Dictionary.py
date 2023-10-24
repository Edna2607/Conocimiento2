""" --------------------- DICCIONARIOS -----------------------

1- hacen parte de colecciones o estructuras de datos que permiten tener = clave y valor
2- son cambiables
3- NO permiten duplicados
4- Desde Python 3.7 son ordenados, versiones anteriores no lo son
5- Permiten agregar  y remover items
6- son iterables 
7- Poseen distintos metodos para manipular los datos
8- Admite distintos tipos de datos"""


usuario = {"nombre":"Pepito", "apellido" : "Perez", "edad" : "25 años"}
print(usuario)


print("--------------------------------------------------------------")
#----------------------------------------------------------------------
#Imprime las claves
print(usuario.keys())


print("--------------------------------------------------------------")
#----------------------------------------------------------------------
#Imprime los valores
print(usuario.values())


print("--------------------------------------------------------------")
#----------------------------------------------------------------------
#Para conocer el tamaño del diccionario utilizamos el metodo : len

print(len(usuario))
print(type(usuario))

print("--------------------------------------------------------------")
#----------------------------------------------------------------------
#Cuando queremos buscar un item especifico podemos usar get()

print(usuario.get("nombre"))

#hay otra manera con [] y se obtiene el mismo resultado
print(usuario["nombre"])

print("--------------------------------------------------------------")
#----------------------------------------------------------------------
# Agregar nuevos items

usuario["correo"] = "pepito@hotmail.com"

print(usuario.keys())
print(usuario.get("correo"))

print("--------------------------------------------------------------")
#---------------------------------------------------------------------

# Actualizar un valor 

usuario.update({"correo":"peperez@mail.com"})
print(usuario.get("correo"))

print("--------------------------------------------------------------")
#---------------------------------------------------------------------

# Remover = 3 formas  

#usuario.pop("nombre")
#print(usuario.keys())

#usuario.popitem() ----> borra el ultimo item
#print(usuario.keys())

#del usuario["edad"]
#print(usuario.keys())

print("--------------------------------------------------------------")
#---------------------------------------------------------------------

# Recorrer el diccionario = podemos elegir entre recorrer las claves, recorrer los valores o recorrer ambos

#AMBOS

for x, y in usuario.items():
    print(x,y)

print("---------------------------")

#Recorrer las claves

for x in usuario.keys():
    print(x)

print("---------------------------")

# Recorrer Valores

for y in usuario.values():
    print(y)

print("--------------------------------------------------------------")
#---------------------------------------------------------------------

# Podemos tener un diccionario de diccionarios

usuarios = { "usuario1":{"nombre":"Juan", "Edad" : 12}, "usuario2":{"nombre": "Maria", "Edad": 15}, "usuario3":{"nombre": "Julia" , "edad": 18}}


#Hay otra manera de crear diccionarios dentro de otro diccionario
estudiante1 = {"nota1":4.2, "nota2":4.3}
estudiante2 = {"nota1":4.4, "nota2":4.3}
estudiante3 = {"nota1":4.5, "nota2":4.1}

estudiantes = {
    "estudiante1": estudiante1,
    "estudiante2": estudiante2,
    "estudiante3": estudiante3
}

print(estudiantes["estudiante2"]["nota2"])