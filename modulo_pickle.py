from pickle import *

def pasa_dic():
	palabras={}
	palabras["ARBOL"]="Pista de Arbol"
	palabras["CASA"]="Pista de casa"
	palabras["SILLA"]="Pista de silla"
	palabras["AUDIO"]="Pista de audio"
	palabras["VENTANA"]="Pista de ventana"
	palabras["COMPUTADORA"]="Pista de computadora"
	palabras["RELOJ"]="Pista de reloj"
	palabras["AVION"]="Pista de avion"
	palabras["MILANESA"]="Pista de milanesa"
	
	pickle_file = open('palabras.pickle', 'wb')
	dump(palabras, pickle_file)

	pickle_file = open('palabras.pickle','rb')
	contenido_dic = load(pickle_file)

	return contenido_dic