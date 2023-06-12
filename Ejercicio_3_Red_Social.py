"""
RED SOCIAL:
Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de tuplas, donde cada tupla contiene 
el nombre del usuario y una lista de sus amigos. Los nombres repetidos en la lista de amigos corresponden a usuarios 
con varias cuentas diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de tuplas que 
contiene el número real de amigos por usuario y el usuario con más amigos.
Pista 1: Tus datos de entrada podrían ser así —> 
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]
Pista 2: Para eliminar duplicidades puedes usar sets
"""
#definimos la base de datos
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]
print("------------")
print("La base de datos es:")
print(red_social)

#utizamos compresion de listas. a partir de la estructura base de la lista "red_social = [([tupla,[lista])]"
#convertimos la lista en un set, luego en una lista y luego contamos la longitud de la lista de amigos 
red_social_sin_duplicados = [(nombre, len(list(set(amigos)))) for nombre, amigos in red_social] 
print("------------")
print("El listado de usuarios con la cantidad de amigos sin duplicados es:")
print(red_social_sin_duplicados)

#creamos una lista vacia para llenarla con la cantidad total de amigos y asi calcular el maximo
lista = []

#utizamos compresion de listas para agregar la cantidad de amigos a la lista "lista"
[(nombre, (lista.append(cant_amigos))) for nombre, cant_amigos in red_social_sin_duplicados]

#determinamos cual es la cantidad maxima de amigos, que en este caso es 3
max_amigos = max(lista)

#utizamos compresion de listas para recorrer la base de datos y comparar que usuario coincide con la cantidad maxima de amigos
#usuario_maximo es una lista, que contiene una tupla y que dentro de esa tupla hay en la posicion 0 un string y un integer en la posicion 1
usuario_maximo = [(nombre, cant_amigos) for nombre, cant_amigos in red_social_sin_duplicados if cant_amigos == max_amigos] 

#imprimimos el resultado
print("------------")
print("El usuarios que tiene más amigos es:", usuario_maximo[0][0]) 
print("La cantidad de amigos que tiene es:", usuario_maximo[0][1])
print("------------")