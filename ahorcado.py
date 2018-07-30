import random
from PyQt5 import QtWidgets, QtGui
from ahorcado_qt import Ahorcado_Qt


class Ahorcado(QtWidgets.QMainWindow,Ahorcado_Qt):
	palabra_aleatoria = ""
	incognita = []
	letra = ""
	intentos = 6

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.lista_palabra()
		self.inicia_partida()
		self.puntuacion = 0
		self.pista = ""
		self.vidas = 3


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
		

		#Boton pista y arriesgar
		self.boton_pista.clicked.connect(self.devuelve_pista)
		self.boton_arriesgar.clicked.connect(self.arriesgar)



	def inicia_partida(self):
		self.buscar_palabra_aleatoria()
		self.incognita = []
		self.devuelve_incognita()
		self.intentos = 6
		self.imagen_ahorcado()


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
		boton = self.sender()
		diccionario = modulo_pickle.pasa_dic()
		self.pista = diccionario.get(self.palabra_aleatoria)
		self.etiqueta_pista.setText(self.pista)
		self.etiqueta_pista.setWordWrap(True)
		self.puntuacion -= 40
		self.actualiza_puntuacion()
		boton.setEnabled(False)

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
		self.letra = boton.text()
		#boton.text() devuelve la letra presionada
		#si esta en la palabra retorna true, si no, else
		pos = len(self.palabra_aleatoria)-1
		if self.letra in self.palabra_aleatoria[1:pos]:
			self.reemplaza_guion()
			self.boton_verde()
			
			
			return True
		else:
			self.intentos -= 1
			self.boton_rojo()
			self.imagen_ahorcado()
			self.cuenta_intentos()
			return False
		

	#Reemplaza en la incognita el guion por la letra presionada
	def reemplaza_guion(self):
		for i in range(len(self.palabra_aleatoria)):
			if(self.letra == self.palabra_aleatoria[i]):
				self.incognita[i] = self.letra
				self.etiqueta_incognita.setText(' '.join(self.incognita))
				self.puntuacion += 30
				self.actualiza_puntuacion()

	
	#Desactiva el boton y cambia a color verde si la letra esta en la incognita
	def boton_verde(self):
		boton = self.sender()
		boton.setEnabled(False)
		boton.setStyleSheet("QPushButton{background-color: green; color: black;border: 1px solid gray;}")

	#Suma 30 puntos si la letra esta en la incognita


	#Desactiva el boton y cambia a color rojo si la letra no esta en la incognita
	def boton_rojo(self):
		boton = self.sender()
		boton.setEnabled(False)
		boton.setStyleSheet("QPushButton{background-color: red; color: black;border: 1px solid gray;}")


	#Agrega una parte del cuerpo al muñeco si la letra no esta en la incognita
	def imagen_ahorcado(self):
		ahorcado_imagen = ["img/1.jpg","img/2.jpg","img/3.jpg","img/4.jpg","img/5.jpg","img/6.jpg","img/7.jpg"]
		ahorcado_imagen.sort(reverse=True)
		for i in range(self.intentos+1):
			self.etiqueta_imagen.setPixmap(QtGui.QPixmap(ahorcado_imagen[i]))
		

	def actualiza_puntuacion(self):
		self.etiqueta_puntuacion.setText(str(self.puntuacion))


	#Boton arriesgar
	def arriesgar(self):
		#comparo si es igual a la incognita
		if self.entrada_arriesgar.text().upper() == self.palabra_aleatoria:
			#Sumo 50 puntos por cada _ que hay en la incognita
			for i in self.incognita:
				if i == "_":
					self.puntuacion +=50

			self.incognita = self.palabra_aleatoria
			self.etiqueta_incognita.setText(' '.join(self.incognita))

			#Sumo 100 por arriesgar
			self.puntuacion += 100

			self.actualiza_puntuacion()
			self.inicia_partida()
		else:
			self.vidas -= 1
			self.actualiza_vidas()
			self.perdiste_vida()


	def actualiza_vidas(self):
		if self.vidas == 3:
			self.etiqueta_vidas.setText("❤❤❤")
		elif self.vidas == 2:
			self.etiqueta_vidas.setText("❤❤")
		elif self.vidas == 1:
			self.etiqueta_vidas.setText("❤")


	def cuenta_intentos(self):
		if self.intentos == 0:
			self.vidas -= 1
			self.perdiste_vida()
			self.actualiza_vidas()

	def perdiste_vida(self):
		respuesta = QtWidgets.QMessageBox.information(self, "Perdiste una vida", "La palabra era: "+self.palabra_aleatoria+"\nTe quedan "+str(self.vidas)
		 	+" vidas",
		QtWidgets.QMessageBox.Ok)
		if respuesta == QtWidgets.QMessageBox.Ok:
			self.inicia_partida()
		