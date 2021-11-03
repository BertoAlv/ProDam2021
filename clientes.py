'''

Funciones gestion clientes

'''
import conexion
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
                    var.ui.txtDNI.setStyleSheet('background-color: white')
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
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra']
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
            newcli = []
            cliente=[var.ui.txtDNI,var.ui.txtFchAlta,var.ui.txtApel,var.ui.txtNome,var.ui.txtDir]  #Para base de datos
            tabcli = []   #Para table widget
            client =[var.ui.txtDNI,var.ui.txtApel,var.ui.txtNome,var.ui.txtFchAlta]
            #Codigo para cargar en la tabla
            for i in cliente:
                newcli.append(i.text())
            for i in client:
                tabcli.append(i.text())
            newcli.append(var.ui.cmbProv.currentText())
            newcli.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHom.isChecked():
                newcli.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                newcli.append('Mujer')
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
            newcli.append(', '.join(pagos))
            tabcli.append(', '.join(pagos))
            print(newcli)
            if dnivalido:
                conexion.Conexion.altaCli(newcli)
                conexion.Conexion.cargarTabCli(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI no valido')
                msg.exec()
            #Codigo para grabar en la base de datos
        except Exception as error:
            print('Error en guardar clientes ', error)

    def bajaCli(self):
        try:
            dni = var.ui.txtDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargarTabCli(self)

        except Exception as error:
            print('Error en baja cliente ',error)

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

    def cargaCli(self):
        try:
            Clientes.limpiaFormCli(self)
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtFchAlta]
            if fila:
                row = [dato.text() for dato in fila]
            print(row)
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in row[4]:
                var.ui.chkTransferencia.setChecked(True)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Cargo' in row[4]:
                var.ui.chkCargocuenta.setChecked(True)

            registro = conexion.Conexion.oneCli(row[0])
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMuni.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            else:
                var.ui.rbtFem.setChecked(True)

        except Exception as error:
            print('Error en cargar los datos del cliente', error)
