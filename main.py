# This is a sample Python script.
import sys
import eventos
import clientes
import var
from datetime import *
from ventana import *
from windowaviso import *
from windowcal import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        dia_actual = datetime.now().day
        mes_actual = datetime.now().month
        ano_actual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(ano_actual,mes_actual,dia_actual)))
     #   var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargarFecha)

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
        var.ui.btnFchAlta.clicked.connect(eventos.Eventos.abrirCal)
#Eventos de la barra de menús
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
#Eventos de texto
        var.ui.txtDNI.editingFinished.connect(clientes.Clientes.validarDNI)
#Eventos de comboBox
        clientes.Clientes.cargaProv_(self)
        var.ui.cmbProv.activated[str].connect(clientes.Clientes.selProv)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    ventana.show()
    sys.exit(app.exec())
