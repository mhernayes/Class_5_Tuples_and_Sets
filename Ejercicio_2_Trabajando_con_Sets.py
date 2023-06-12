"""
14.Crea un set y elimina uno de sus elementos.
15.Crea un set vacío.
16.Crea dos sets y encuentra su union, su intersección y su diferencia.
17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.
18.Crea un script que dado un set con números devuelva el numero máximo y mínimo.
19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets.
20.Crea un set con colores y comprueba si es cierto que color se encuentra en el set.
21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo.
22.Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.
"""
import numpy as np

#14.Crea un set y elimina uno de sus elementos.
print("-------------")
set_14 = {1,2,3,4}
set_14.remove(4) #utilizamos el metodo remove para eliminar un valor
print(set_14)

#15.Crea un set vacío.
print("-------------")
set_vacio = set()
print(set_vacio)
print(type(set_vacio))

#16.Crea dos sets y encuentra su union, su intersección y su diferencia.
print("-------------")
set_16 = {3,4,5,6,7} 
set_16_bis = {1,2,3,4,5}
print("El set 1 es:", set_16)
print("El set 2 es:", set_16_bis)
intersection = set_16.intersection(set_16_bis) #utilizamos el metodo intersection para veriticar los valores repetidos
union = set_16.union(set_16_bis)
diferencia = set_16.difference(set_16_bis)
print("La interseccion es:", intersection)
print("La union es:", union)
print("La diferencia es:", diferencia)

#17.Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.
print("-------------")
set_17 = {4,5,6,7,8}
set_17_bis = {1,2,3,4,5}
print("El set 1 es:", set_17)
print("El set 2 es:", set_17_bis)
intersection = set_17.intersection(set_17_bis) #utilizamos el metodo intersection para veriticar los valores repetidos
print("Los elementos comunes de ambos son:", intersection)

#18.Crea un script que dado un set con números devuelva el numero máximo y mínimo.
print("-------------")
set_18 = {4,5,6,7,8}
maximo = max(set_18)
minimo = min(set_18)
print("El numero maximo del set:", set_18, "es:", maximo)
print("El numero minimo del set:", set_18, "es:", minimo)

#19.Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets.
print("-------------")
set_19 = {3,4,5,6,7} 
set_19_bis = {1,2,3,4,5}
print("El set 1 es:", set_19)
print("El set 2 es:", set_19_bis)
diferencia_simetrica = set_19.symmetric_difference(set_19_bis) #utilizamos el metodo de diferencia simetrica crear un array solo con los elementos unicos
print("La diferencia simetrica es:", diferencia_simetrica)

#20.Crea un set con colores y comprueba si es cierto que color se encuentra en el set.
print("-------------")
set_20 = {"rojo", "verde", "azul"}
while True:
    color = str(input("Por favor, ingrese un color:\n"))
    if color in set_20:
        print("El color ingresado:", color, "se encuentra en el Set:", set_20)
        break
    else:
        print("El color ingresado:", color, "NO encuentra en el Set:", set_20)
        break

#21.Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo.
print("-------------")
set_21 = {0,1,2,3,4,5}
set_21_bis = {4,5,6,7,8,9}
print("El set 1 es:", set_21)
print("El set 2 es:", set_21_bis)
diferencia = set_21.difference(set_21_bis) #utilizamos el metodo de diferencia simetrica crear un array solo con los elementos unicos
print("La diferencia es:", diferencia)

#22.Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.
set_22 = {1,2,3,4,5}
array_22 = np.array(list(set_22)) #primero se debe convertir el set a lista y despues a un array porque en numpy no se puede pasar como argumento un set
producto = np.prod(array_22)
print("El resultado de la multiplicacion de todos los elementos del Set es:", producto)