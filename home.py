import sys
import webbrowser

from ferramentas import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from organizar import Organizar
from time import sleep


class Home(QMainWindow, Ferramentas, Organizar):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().carregarModal(self)

        self.local = ''
        self.log = list()
        self.btn_escolher.clicked.connect(self.escolherPasta)
        self.btn_organizar.clicked.connect(self.organizarPasta)
        self.btn_log.clicked.connect(self.abrirLog)
        self.msg_sucesso.setText(' ')

    def escolherPasta(self):
        self.local = QFileDialog.getExistingDirectory()
        print(self.local)

    def organizarPasta(self):
        if len(self.local) == 0:
            print('escolha a pasta')
            self.msg_sucesso.setText('Escolha uma pasta')
        else:
            org = Organizar(self.local)
            org.organizando()
            self.msg_sucesso.setText('Finalizado com sucesso!')

    def abrirLog(self):
        if len(self.local) == 0:
            self.msg_sucesso.setText('Escolha uma pasta')
        else:
            org = Organizar(self.local)
            org.abrirLog()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    home = Home()
    home.show()
    qt.exec_()
