import os.path
import sys
import zipfile
import shutil
import var
from ventana import *
from datetime import date, datetime
from zipfile import ZipFile
import conexion
from PyQt5 import QtPrintSupport

class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en módulo salir ', error)

    def abrirCal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir calendario',error)

    def resizeTabClientes(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                     header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en resize de la tabla',error)

    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error en módulo abrir', error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Backup')
            msg.setModal(True)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Backup creado con éxito')
            msg.exec()

        except Exception as error:
            print('Error Crear Backup', error)

    def restaurarBD(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Datos', '', '*.zip',options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichero = filename[0]
                print(fichero)
                with zipfile.ZipFile(str(fichero),'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli(self)
            conexion.Conexion.cargaProv(self)
            conexion.Conexion.cargaMuni(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Backup')
            msg.setModal(True)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Backup creado con éxito')
            msg.exec()
        except Exception as error:
            print('Error al restaurar la BD desde el backup',error)

    def Imprimir(self):
        try:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec():
                printDialog.show()
        except Exception as error:
            print('Error imprimir',error)