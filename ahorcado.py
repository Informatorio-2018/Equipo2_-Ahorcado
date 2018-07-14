import random
from PyQt5 import QtWidgets
from ahorcado_qt import Ahorcado_Qt

class Ahorcado(QtWidgets.QMainWindow,Ahorcado_Qt):
	palabra_aleatoria = ""

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.lista_palabra()
		self.buscar_palabra_aleatoria()
		self.devuelve_pista()
		self.devuelve_incognita()


		#Conecta los botones
		

	def lista_palabra(self):
		import modulo_pickle
		diccionario=modulo_pickle.pasa_dic()
		lista=list(diccionario.keys())
		return lista

	def buscar_palabra_aleatoria(self):
		lista_de_palabras=self.lista_palabra()
		self.palabra_aleatoria=random.choice(lista_de_palabras)
		
		

	def devuelve_pista(self):
		import modulo_pickle
		diccionario = modulo_pickle.pasa_dic()
		pista = diccionario.get(self.palabra_aleatoria)
		# self.etiqueta_pista.setText(pista)
		

	def devuelve_incognita(self):
		incognita = []
		for i in range(len(self.palabra_aleatoria)):

			if(i == 0):
				incognita.append(self.palabra_aleatoria[0])
			elif(i == len(self.palabra_aleatoria)-1):
				incognita.append(self.palabra_aleatoria[len(self.palabra_aleatoria)-1])
			else:
				incognita.append("_")

		self.etiqueta_incognita.setText(' '.join(incognita))
	
	

