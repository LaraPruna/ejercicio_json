from funciones_json import LeerJson
opcion=input('''Elige una opción del siguiente menú:
1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir''')
while opcion<1 and opcion>6:
	print("Error. Introduce el número de la opción correcta.")
	opcion=input('''Elige una opción del siguiente menú:
1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir''')
while opcion!=6:
	if opcion==1:
	elif opcion==2:
	elif opcion==3:
	elif opcion==4:
	else:
	opcion=input('''Elige una opción del siguiente menú:
1. Lista de películas
2. Número de películas por categoría
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir''')