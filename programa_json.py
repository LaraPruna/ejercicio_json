from funciones_json import LeerJson,ListaPelis
opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))
while opcion<1 and opcion>6:
	print("Error. Introduce el número de la opción correcta.")
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))
while opcion!=6:
	if opcion==1:
		print(ListaPelis())
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))