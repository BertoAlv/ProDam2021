# This is a sample Python script.
import sys
import eventos
import clientes
import var
from ventana import *
from windowaviso import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accept)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_window()
        var.ui.setupUi(self)

#Eventos de botón
        var.ui.btnSalir.clicked.connect(eventos.Eventos.Salir)
        var.ui.rbtGroupSex.buttonClicked.connect(clientes.Clientes.SelSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clientes.Clientes.selPago)
#Eventos de la barra de menús
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
#Eventos de texto
        var.ui.txtDNI.editingFinished.connect(clientes.Clientes.validarDNI)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = Main()
    var.dlgaviso = DialogAviso()
    ventana.show()
    sys.exit(app.exec())
