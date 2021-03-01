import json

def LeerJson():
	try:
		with open("vengadores.json") as fichero:
			datos=json.load(fichero)
		return datos
	except:
		print("Error al cargar el fichero.")