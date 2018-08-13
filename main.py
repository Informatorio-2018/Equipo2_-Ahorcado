import sys
from PyQt5.QtWidgets import QApplication
from ahorcado import Ahorcado

app = QApplication(sys.argv)

ahorcado = Ahorcado()

sys.exit(app.exec_())