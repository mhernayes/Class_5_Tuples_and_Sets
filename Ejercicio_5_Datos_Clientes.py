"""
DATOS CLIENTES:
Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene el nombre del cliente, 
la dirección de correo electrónico y el número de teléfono. La segunda base de datos contiene el nombre del cliente, 
la dirección y el historial de pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y 
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en ambas bases de datos. Los clientes 
se consideran iguales si tienen el mismo nombre.
Pista: Tus datos de entrada podrían ser así —>
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")] 
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]
"""

base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"),("Pedro", "pedro@example.com", "555-9012")]
base_datos2 = [("Maria", "Calle 123", ["Libro1", "Libro2"]), ("Juan", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

#recorro ambas listas para quedarme unicamente con los datos de los clientes que se encuentran en ambas listas  
base_unificada_1 = [(nombre, mail, telefono) for (nombre, mail, telefono) in base_datos1 if nombre in [nombre_base2[0] for nombre_base2 in base_datos2]] #nombre_bsae2[0] son los nombres (Juan, Maria, Luis)
base_unificada_2 = [(nombre, direccion, libros) for (nombre, direccion, libros) in base_datos2 if nombre in [nombre_base1[0] for nombre_base1 in base_datos1]]

#ordeno los datos para asegurarme que al unificar las listas tenga en cuenta el orden correcto
base_unificada_1.sort() 
base_unificada_2.sort()

#con la funcion zip agrupo los datos del mismo nombre
for base_unificada_1, base_unificada_2 in zip(base_unificada_1, base_unificada_2):
    print("-----")
    print("Nombre: {}".format(base_unificada_1[0]))
    print("Mail: {}".format(base_unificada_1[1]))
    print("Telefono: {}".format(base_unificada_1[2]))
    print("Direccion: {}".format(base_unificada_2[1]))
    print("Libros: {}".format(base_unificada_2[2]))
    print("-----")

"""
Explicacion de la compresion de listas utilizada y como comparar 2 listas con subtuplas
1. Se crea una lista base_unificada vacía para almacenar las tuplas unificadas.
2. Se itera a través de cada tupla (nombre, mail, telefono) en base_datos1.
3. Si el nombre de la tupla está en la lista de nombres [nombre_base2[0] for nombre_base2 in base_datos2], 
se agrega la tupla a base_unificada.
4. La expresión [nombre_base2[0] for nombre_base2 in base_datos2] crea una lista que contiene el primer 
elemento (el nombre) de cada tupla en base_datos2. 

Esta lista se utiliza para verificar si el nombre de la tupla de base_datos1 se encuentra en base_datos2.
"""