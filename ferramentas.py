from PyQt5 import QtCore, QtWidgets


class Ferramentas(object):
    def carregarModal(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 250)

        self.tab = QtWidgets.QWidget()
        self.tabWidget = QtWidgets.QTabWidget(Dialog)

        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.btn_organizar = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_escolher = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_log = QtWidgets.QPushButton(self.tab)
        self.msg_sucesso = QtWidgets.QLabel(self.tab)

        self.tab.setObjectName("tab")
        self.tabWidget.setObjectName("tabWidget")
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout.setObjectName("formLayout")
        self.btn_escolher.setObjectName("btn_escolher")
        self.btn_organizar.setObjectName("btn_organizar")
        self.msg_sucesso.setObjectName("msg_sucesso")
        self.btn_log.setObjectName("btn_log")

        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 300, 210))
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 10, 160, 70))
        self.msg_sucesso.setGeometry(QtCore.QRect(70, 80, 160, 13))
        self.btn_log.setGeometry(QtCore.QRect(70, 120, 160, 23))

        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.btn_escolher)
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.btn_organizar)

        self.tabWidget.addTab(self.tab, "")

        self.carregarTexto(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def carregarTexto(self, Dialog):
        texto = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(texto("Dialog", "Organizador de pastas"))

        self.btn_escolher.setText(
            texto("Dialog", "SELECIONAR PASTA"))
        self.btn_organizar.setText(texto("Dialog", "INICIAR"))
        self.msg_sucesso.setText(texto("Dialog", "."))
        self.btn_log.setText(
            texto("Dialog", "ABRIR LOG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), texto("Dialog", "Organizar arquivos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ferramentas()
    ui.carregarModal(Dialog)
    Dialog.show()
