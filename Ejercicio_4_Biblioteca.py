"""
LA BIBLIOTECA:
Una biblioteca tiene una lista de libros y sus autores. 
Crea un programa que tome la lista de libros y sus autores como una lista de tuplas, 
donde cada tupla contiene el título del libro y el nombre del autor, y devuelva una nueva 
lista de tuplas que contenga el título del libro y el apellido del autor.
Pista: Tus datos de entrada podrían ser así —> 
lista_libros = [(‘El aleph', ‘Jorge Luis Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros', ‘Mario Vargas Llosa')]
"""
#definimos la lista 
lista_libros = [("El aleph", "Jorge Luis Borges"), ("Cien años de soledad", "Garbriel Garcia Márquez"), ("La ciudad y los perros", "Mario Vargas Llosa")]

#con el metodo compresion de lista nos quedamos con el apellido de cada autor
lista_libro_apellidos = [(nombre, (apellido[(apellido.rfind(" ")):])) for nombre, apellido in lista_libros]

#imprimimos la lista
print("------------")
print("La lista de libros con los apellidos es:")
print(lista_libro_apellidos)
print("------------")
