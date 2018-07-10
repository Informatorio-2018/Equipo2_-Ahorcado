from pickle import * 
from modulo_pickle import *
import random


class Ahorcado():

	def lista_palabra(self):
		diccionario=pasa_dic()
		lista=list(diccionario.keys())
		return lista

	def buscar_palabra_aleatoria(self):
		lista_de_palabras=self.lista_palabra()
		palabra_aleatoria=random.choice(lista_de_palabras)
		return palabra_aleatoria




ahorcado1=Ahorcado()

print(ahorcado1.lista_palabra())
print()
print()

print(ahorcado1.buscar_palabra_aleatoria())

input('')




