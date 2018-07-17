import random
from PyQt5 import QtWidgets
from ahorcado_qt import Ahorcado_Qt

class Ahorcado(QtWidgets.QMainWindow,Ahorcado_Qt):
	palabra_aleatoria = ""
	incognita = []

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.lista_palabra()
		self.buscar_palabra_aleatoria()
		self.devuelve_pista()
		self.devuelve_incognita()


		#Conecta los botones(letras)
		self.letra_a.clicked.connect(self.letra_presionada)
		self.letra_b.clicked.connect(self.letra_presionada)
		self.letra_c.clicked.connect(self.letra_presionada)
		self.letra_d.clicked.connect(self.letra_presionada)
		self.letra_e.clicked.connect(self.letra_presionada)
		self.letra_f.clicked.connect(self.letra_presionada)
		self.letra_g.clicked.connect(self.letra_presionada)
		self.letra_h.clicked.connect(self.letra_presionada)
		self.letra_i.clicked.connect(self.letra_presionada)
		self.letra_j.clicked.connect(self.letra_presionada)
		self.letra_k.clicked.connect(self.letra_presionada)
		self.letra_l.clicked.connect(self.letra_presionada)
		self.letra_m.clicked.connect(self.letra_presionada)
		self.letra_n.clicked.connect(self.letra_presionada)
		self.letra_enie.clicked.connect(self.letra_presionada)
		self.letra_o.clicked.connect(self.letra_presionada)
		self.letra_p.clicked.connect(self.letra_presionada)
		self.letra_q.clicked.connect(self.letra_presionada)
		self.letra_r.clicked.connect(self.letra_presionada)
		self.letra_s.clicked.connect(self.letra_presionada)
		self.letra_t.clicked.connect(self.letra_presionada)
		self.letra_u.clicked.connect(self.letra_presionada)
		self.letra_v.clicked.connect(self.letra_presionada)
		self.letra_w.clicked.connect(self.letra_presionada)
		self.letra_x.clicked.connect(self.letra_presionada)
		self.letra_y.clicked.connect(self.letra_presionada)
		self.letra_z.clicked.connect(self.letra_presionada)
		



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
		
		for i in range(len(self.palabra_aleatoria)):

			if(i == 0):
				self.incognita.append(self.palabra_aleatoria[0])
			elif(i == len(self.palabra_aleatoria)-1):
				self.incognita.append(self.palabra_aleatoria[len(self.palabra_aleatoria)-1])
			else:
				self.incognita.append("_")

		self.etiqueta_incognita.setText(' '.join(self.incognita))
	
	

	def letra_presionada(self):
		#recupera la señal que envia el boton al presionar
		boton = self.sender()

		#boton.text() devuelve la letra presionada
		#si esta en la palabra retorna true, si no, else
		if boton.text() in self.palabra_aleatoria:
			for i in range(len(self.palabra_aleatoria)):
				if(boton.text() == self.palabra_aleatoria[i]):
					self.incognita[i] = boton.text()
					self.etiqueta_incognita.setText(' '.join(self.incognita))
			return True
		else:
			return False
		

	# #No se como hacer para que se ejecute este metodo
	# def reemplaza_guion(self):
	# 	boton = self.sender()
	# 	if self.letra_presionada():
	# 		for i in range(len(self.palabra_aleatoria)):
	# 			if(self.boton.text() == self.palabra_aleatoria[i]):
	# 				self.incognita[i] = self.boton.text()
	# 				self.etiqueta_incognita.setText(' '.join(self.incognita))

	
