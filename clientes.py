'''

Funciones gestion clientes

'''
import var
from ventana import *

class Clientes():
    def validarDNI():
        try:
            dni = var.ui.txtDNI.text()
            var.ui.txtDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE' #letras DNI
            dig_ext = 'XYZ'                   #digito documento extranjero
            reemp_dig_ext = {'X': '0', 'Y':'1', 'Z':'2' }
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValidoDNI.setText('V')
                else:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValidoDNI.setText('X')
                    var.ui.txtDNI.setStyleSheet('background-color: pink')
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidoDNI.setText('X')
                var.ui.txtDNI.setColor('background-color: pink')
        except Exception as error:
            print('Error modulo validacion dni', error)

    def SelSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado mujer')
            if var.ui.rbtHom.isChecked():
                print('Marcado hombre')
        except Exception as error:
            print('Error en módulo seleccionar sexo', error)

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Has seleccionado efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Has seleccionado pago con tarjeta')
            if var.ui.chkTransferencia.isChecked():
                print('Has seleccionado transferencia')
            if var.ui.chkCargocuenta.isChecked():
                print('Has seleccionado cargo cuenta')
        except Exception as error:
            print('Error en módulo seleccionar forma de pago', error)