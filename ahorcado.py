import random
from PyQt5 import QtWidgets
from ahorcado_qt import Ahorcado_Qt

class Ahorcado(QtWidgets.QMainWindow,Ahorcado_Qt):
	palabra_aleatoria = ""

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		#Conecta los botones
		self.letra_a.clicked.connect(self.numero_presionado)

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
		for i in self.palabra_aleatoria:
			incognita.append("_")
		incognita[0] = self.palabra_aleatoria[0]
		incognita[len(incognita)-1] = self.palabra_aleatoria[len(self.palabra_aleatoria)-1]
		return incognita 


	def numero_presionado(self):
		global incognita
		boton = self.sender().text()
		a = str(self.devuelve_incognita())
		self.etiqueta_incognita.setText(incognita)
	

