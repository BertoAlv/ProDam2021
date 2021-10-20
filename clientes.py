'''

Funciones gestion clientes

'''
import eventos
import var
from ventana import *

class Clientes():
    def validarDNI():
        try:
            global dnivalido
            dnivalido = False
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
                    dnivalido = True
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

    def cargaProv_(self):
        try:
            var.ui.cmbProv.clear()
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra','Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en módulo cargar provincias', error)

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error en la seleccion de provincia', error)

    def cargarFecha(qDate):
        try:
            data= ('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtFchAlta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha ',error)


    def letracapital():
        try:
            nome = var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.title())
            apelido = var.ui.txtApel.text()
            var.ui.txtApel.setText(apelido.title())
            direccion = var.ui.txtDir.text()
            var.ui.txtDir.setText(direccion.title())
        except Exception as error:
            print('Error en mayuscula', error)

    def guardaCli(self):
        try:
            #preparamos el registro
            newcli=[]  #Para base de datos
            tabcli = []   #Para table widget
            client =[var.ui.txtDNI,var.ui.txtApel,var.ui.txtNome,var.ui.txtFchAlta]
            #Codigo para cargar en la tabla
            for i in client:
                tabcli.append(i.text())
            pagos = []
            if var.ui.chkCargocuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTransferencia.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            pagos = set(pagos) #evita duplicados
            tabcli.append(', '.join(pagos))
            if dnivalido:
                row=0
                column=0
                var.ui.tabClientes.insertRow(row)
                for campo in tabcli:
                    cell=QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row,column,cell)
                    column += 1
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI no valido')
                msg.exec()
            #Codigo para grabar en la base de datos
        except Exception as error:
            print('Error en guardar clientes ', error)

    def limpiaFormCli(self):
        try:
            cajas = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtFchAlta,var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransferencia.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargocuenta.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMuni.setCurrentIndex(0)
        except Exception as error:
            print('Error en guardar clientes', error)