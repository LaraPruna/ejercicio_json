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

