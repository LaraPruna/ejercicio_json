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
	return actores

def FiltroActor(actor):
	for cat in LeerJson().get("categorias"):
		for pel in cat.get("playlist"):
			if actor in pel.get("actors"):
				print(pel.get("titulo"))

def ListaCat():
	categorias=[]
	for cat in LeerJson().get("categorias"):
		categorias.append(cat.get("categoria"))
	return categorias

def FiltroActorCat(categ):
	actores=[]
	for cat in LeerJson().get("categorias"):
		if categ==cat.get("categoria"):
			for pel in cat.get("playlist"):
				for actor in pel.get("actors"):
					if actor not in actores:
						actores.append(actor)
	return actores


def FiltroActorCatTrailer(actor,categ):
	ind=True
	for cat in LeerJson().get("categorias"):
		if categ==cat.get("categoria"):
			for pel in cat.get("playlist"):
				if actor in pel.get("actors") and len(pel.get("trailer"))!=0:
					print("Título: "+pel.get("titulo"))
					print("Trailer: "+pel.get("trailer"))
					ind=False
	if ind:
		print("No hay trailer disponible en ninguna pelicula.")