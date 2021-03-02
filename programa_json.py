from funciones_json import *
opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por superhéroe
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))
while opcion<1 and opcion>6:
	print("Error. Introduce el número de la opción correcta.")
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por superhéroe
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))
while opcion!=6:
	if opcion==1:
		ListaPelis()
		print()
	elif opcion==2:
		ContarPelis()
		print()
	elif opcion==3:
		inicio=int(input("Año de inicio del intervalo: "))
		fin=int(input("Año final del intervalo: "))
		print()
		FiltroIntervalo(inicio,fin)
		print()
	elif opcion==4:
		print("Lista de actores en la base de datos:")
		print()
		for actor in ListaActores():
			print(actor)
		print()
		act=input("Introduce el nombre de un actor de la lista anterior: ")
		while act not in ListaActores():
			print("Ese nombre no se encuentra en la lista.")
			act=input("Introduce el nombre de un actor de la lista anterior: ")
		FiltroActor(act)
		print()
	else:
		print("Lista de categorías en la base de datos: ")
		print()
		for categ in ListaCat():
			print(categ)
		print()
		cat=input("Introduce el nombre de una categoría de la lista anterior: ")
		while cat not in ListaCat():
			print("Esa categoría no se encuentra en la lista.")
			cat=input("Introduce el nombre de una categoría de la lista anterior: ")
		print()
		print("Lista de actores en la categoría "+cat+" :")
		for actor in FiltroActorCat(cat):
			print(actor)
		print()
		act=input("Introduce el nombre de un actor de la lista anterior: ")
		while actor not in ListaActores():
			print("Ese nombre no se encuentra en la lista.")
			act=input("Introduce el nombre de un actor de la lista anterior: ")
		print()
		FiltroActorCatTrailer(act,cat)
		print()
	opcion=int(input('''Elige una opción del siguiente menú:

1. Lista de películas
2. Número de películas por superhéroe
3. Buscar películas por intervalo de fechas
4. Buscar películas de un actor en concreto
5. Buscar películas por actor y categoría con tráiler disponible
6. Salir

Opción: '''))

print("Fin del programa.")