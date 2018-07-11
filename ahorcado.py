
import random


class Ahorcado():
	palabra_aleatoria = ""

	def lista_palabra(self):
		import modulo_pickle
		diccionario=modulo_pickle.pasa_dic()
		lista=list(diccionario.keys())
		return lista

	def buscar_palabra_aleatoria(self):
		global palabra_aleatoria
		lista_de_palabras=self.lista_palabra()
		palabra_aleatoria=random.choice(lista_de_palabras)
		return palabra_aleatoria

	def devuelve_pista(self):
		# global palabra_aleatoria
		import modulo_pickle
		diccionario = modulo_pickle.pasa_dic()
		pista = diccionario.get(palabra_aleatoria)
		return pista

	def devuelve_incognita(self):
		incognita = []
		for i in palabra_aleatoria:
			incognita.append("_")
		incognita[0] = palabra_aleatoria[0]
		incognita[len(incognita)-1] = palabra_aleatoria[len(palabra_aleatoria)-1]
		return incognita 




ahorcado1=Ahorcado()

print(ahorcado1.lista_palabra())
print()
print()

print(ahorcado1.buscar_palabra_aleatoria())
print(ahorcado1.devuelve_pista())
print(ahorcado1.devuelve_incognita())


input('')
