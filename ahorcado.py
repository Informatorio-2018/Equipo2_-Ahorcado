from modulo_pickle import *
import random
from pickle import * 



class Ahorcado():
	
	def diccionario(self):
		recibir_dic=pasa_dic()
		return recibir_dic

	def lista_random(self):
		recibir_dic=pasa_dic()
		lista=recibir_dic.keys()
		pal_elegida = random.choice(list(recibir_dic.items()))
		print(pal_elegida[0])
		print(pal_elegida[1])




Ahorcado1=Ahorcado()

print(Ahorcado1.diccionario())
input('')
print()

Ahorcado1.lista_random()

input('')