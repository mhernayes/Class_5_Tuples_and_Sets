"""
TRABJANDO CON TUPLAS:
1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias?
3. Crea una tupla de enteros y devuelve la suma de los elementos.
4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.
5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares.
6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente.
7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).
8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.
9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
10. Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
11. Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).
12. Crea un script que dada una tupla devuelva el contenido en orden revertido.
13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente.
"""
import numpy as np

# 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
tupla_1 = (1,2,3)
print(tupla_1[0])
print(tupla_1[1])
print(tupla_1[2])

#2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias?
lista_1 = [1,2,3]
lista_1[0] = 3
print(lista_1)

#La tupla no puede ser modificada
#tupla_1[0] = 3
#print(tupla_1)

#3. Crea una tupla de enteros y devuelve la suma de los elementos.
tupla_3 = (1,2,3)
suma = sum(tupla_3)
print(suma)

#4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.
tupla_4 = ("hola", "como", "estas") #definimos la tupla
lista_4 = [] #creamos una lista vacia
for i in range(0,len(tupla_4)): #recorremos la tupla y cada elemento lo agregamos a la lista
    lista_4.append(tupla_4[i][0])
tupla_4_bis = tuple(lista_4) #creamos una nueva tupla con la lista de los caracteres agregados a la lista 
print("La nueva tupla es", tupla_4_bis)  #imprimimos la nueva tupla

#5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares.
tupla_5 = (1,2,3,4,5,6,7,8,9,10) #definimos la tupla
lista_pares = [num for num in tupla_5 if num % 2 == 0] #creamos una lista solo con los numeros pares con el metodo de compresion 
print("Los numeros pares son:", lista_pares) #imprimimos la lista lsita_pares
array_5 = np.array(lista_pares) #convertimos esta lista en un array
multiplicacion = np.prod(array_5) #realizamos la multiplicacion de todos los elementos pares
print("La multiplicacion es:", multiplicacion) #imprimimos el resultado

#6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente.
tupla_6 = (1,2,3,4,5,6,7,8,9,10) #definimos la tupla
tupla_6_revertida = tuple(reversed(tupla_6)) #aplicamos la funcion reversed a la tupla_6 y lo convertimos nuevamente en una tupla
print("La tupla original es:", tupla_6, "y la tupla revertida es:", tupla_6_revertida)

#7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).
tupla_7 = (1,2,3,4,5,6,7,8,9,10,2,4,5,6,7,7,10,4,5,6) #definimos la tupla
tupla_7_bis = tuple((set(tupla_7))) #convertimos la tupla en un set para eliminar los duplicados y luego lo convertimos en una tupla
print("La tupla original es:", tupla_7, "y la tupla sin duplicados es:", tupla_7_bis)

#8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.
tupla_8 = (1,2,3,4) #definimos una tupla
while True: #utilizamos el while true para que repita el bucle hasta que ingrese un numero
    try: #con un try except controlamos lo que ingresamos de forma incorrecta
        numero = int(input("Ingrese un numero:\n"))
        if numero in tupla_8:
            print("El número ingresado está en la tupla")
            break
        else:
            print("El número ingreado no está en la tupla")
            break
    except:
        print("No ha ingresado un número")

#9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
tupla_9 = (1,2,3,4)
tupla_9_bis = (5,6,7,8)
tupla_9_extend = tupla_9 + tupla_9_bis #al sumar tuplas se unen, no se puede utilizar extend ya que son inmutables
print(tupla_9_extend)

#10. Crea un script que dada una tupla de números devuelva el máximo y el mínimo.
tupla_10 = (1,2,3,4)
tupla_10_bis = ("manzana", "pera")
minimo = min(tupla_10)
maximo = max(tupla_10)
minimo_bis = min(tupla_10_bis, key = len) #para ver cual string es más corto
maximo_bis = max(tupla_10_bis, key = len) #para ver cual string es más largo
print("El numero minimo es:", minimo, "de la tupla:", tupla_10)
print("El numero maximo es:", maximo, "de la tupla:", tupla_10)
print("El string minimo es:", minimo_bis, "de la tupla:", tupla_10_bis)
print("El string maximo es:", maximo_bis, "de la tupla:", tupla_10_bis)

#11. Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. 
# (Prueba añadiendo key=len a las funciones max y min).
tupla_11 = ("hola", "como", "te", "sentis", "?")
minimo = min(tupla_11, key=len)
maximo = max(tupla_11, key=len)
print("El numero minimo es:", minimo, "de la tupla:", tupla_11)
print("El numero maximo es:", maximo, "de la tupla:", tupla_11)

#12. Crea un script que dada una tupla devuelva el contenido en orden revertido.
tupla_12 = ("hola", "como", "te", "sentis", "?")
tupla_12_revertida = tuple(reversed(tupla_12))
tupla_12_revertida_bis = tupla_12[::-1] #otro metodo es hacerlo asi
print("La tupla original es:", tupla_12, "y la tupla revertida es:", tupla_12_revertida)
print("Con otro metodo, la tupla original es:", tupla_12, "y la tupla revertida es:", tupla_12_revertida_bis)

#13. Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, 
# devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente.
tupla_13 = ((10, 0), (11, 1), (12, 2), (13, 3), (14, 4)) #definimos la tupla de tuplas
tupla_13_bis = [] #creamos una lista vacia que usaremos para ir añadiendo las suma de las tuplas
for i in range(len(tupla_13)): #con el for recorremos la tupla y vamos guardando las sumas de las tuplas y agregandolas a la lista
    suma = sum(tupla_13[i])
    tupla_13_bis.append(suma)
tupla_13_bis = tuple(tupla_13_bis) #convertimos la lista en tupla
print("La tupla original es:", tupla_13)
print(type(tupla_13_bis))
print("La tupla con la sumas de cada sub tupla es:", tupla_13_bis)

#Con el metodo de compresion de lista:
tupla_13_bis_2 = tuple(sum(tupla_interna) for tupla_interna in tupla_13)
print("Con otro metodo, calculamos la tupla con la sumas de cada sub tupla es:", tupla_13_bis_2)
