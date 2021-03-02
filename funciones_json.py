import json

def LeerJson():
	try:
		with open("vengadores.json") as fichero:
			datos=json.load(fichero)
		return datos
	except:
		print("Error al cargar el fichero.")

def ListaPelis():
	for cat in LeerJson().get("categorias"):
		for pel in cat.get("playlist"):
			print(f'''Título: {pel.get("titulo")}
Año de estreno: {pel.get("anio")}''')
			print()

def ContarPelis():
	for cat in LeerJson().get("categorias"):
		if cat.get("categoria")!="Avengers":
			print(cat.get("categoria")+": ")
			print(len(cat.get("playlist")))

def FiltroIntervalo(inicio,fin):
	for cat in LeerJson().get("categorias"):
		for pel in cat.get("playlist"):
			if int(pel.get("anio"))>=inicio and int(pel.get("anio"))<=fin:
				print("Título: "+pel.get("titulo"))
				print("Año de estreno: "+pel.get("anio"))
				print()

def ListaActores():
	actores=[]
	for cat in LeerJson().get("categorias"):
		for pel in cat.get("playlist"):
			for actor in pel.get("actors"):
				if actor not in actores:
					actores.append(actor)
	for elem in actores:
		print(elem)

def FiltroActor(actor):
	for cat in LeerJson().get("categorias"):
		for pel in cat.get("playlist"):
			if actor in pel.get("actors"):
				print(pel.get("titulo"))

def ListaCat():
	for cat in LeerJson().get("categorias"):
		print(cat.get("categoria"))

def FiltroActorCatTrailer(actor,categ):
	for cat in LeerJson().get("categorias"):
		if categ==cat.get("categoria"):
			for pel in cat.get("playlist"):
				if actor in pel.get("actors") and len(pel.get("trailer"))>=1:
					print("Título: "+pel.get("titulo"))
					print("Trailer: "+pel.get("trailer"))