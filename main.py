# This is a sample Python script.
import locale
import sys

import conexion
import eventos
import clientes
import var
from datetime import *
from ventana import *
from windowaviso import *
from windowcal import *
locale.setlocale(locale.LC_ALL, 'es-ES')



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        #Ventana abrir explorador windows
        super(FileDialogAbrir, self).__init__()


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        dia_actual = datetime.now().day
        mes_actual = datetime.now().month
        ano_actual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(ano_actual,mes_actual,dia_actual)))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargarFecha)

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
        var.ui.btnGrabaCli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnLimpiar.clicked.connect(clientes.Clientes.limpiaFormCli)
        var.ui.btnEliminar.clicked.connect(clientes.Clientes.bajaCli)
        var.ui.btnModificar.clicked.connect(clientes.Clientes.modifCli)

#Eventos de la barra de menús y herramientas
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(eventos.Eventos.Abrir)
#Eventos de texto
        var.ui.txtDNI.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clientes.Clientes.letracapital)
        var.ui.txtApel.editingFinished.connect(clientes.Clientes.letracapital)
        var.ui.txtDir.editingFinished.connect(clientes.Clientes.letracapital)
#Eventos de comboBox
        var.ui.cmbProv.activated[str].connect(clientes.Clientes.selProv)
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.cargaMuni)

#Eventos de QTabWidget
        eventos.Eventos.resizeTabClientes(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
#Eventos Base de Datos
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTabCli(self)
        conexion.Conexion.cargaProv(self)
        conexion.Conexion.cargaMuni(self)
#Barra de Estado

        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        today = date.today()
        var.ui.lblFecha.setText(today.strftime("%A, %d de %B de %Y").title())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - ventana.width()) // 2
    y = (desktop.height() - ventana.height()) // 2
    ventana.move(x,y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    ventana.show()
    sys.exit(app.exec())
