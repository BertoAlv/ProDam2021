import locale

from PyQt5 import QtSql, QtWidgets, QtGui
from PyQt5.uic.properties import QtCore

import var


class Conexion():
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos.\n' 'Haz click para continuar',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexion establecida')
                return True
        except Exception as error:
            print('Problemas en conexion', error)

    '''
    Módulos gestión base datos clientes
    '''
    def altaCli(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio) VALUES '
                          '(:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':alta', str(newcli[1]))
            query.bindValue(':apellidos', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            query.bindValue(':envio', int(newcli[9]))

            if query.exec_():
                print('Inserción correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de alta')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Problemas alta cliente',error)

    def bajaCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM clientes WHERE dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                print('Baja correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja cliente en conexion ', error)

    def cargarTabCli(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT dni, apellidos, nombre, alta, pago FROM clientes order by apellidos, nombre')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tabClientes.setRowCount(index+1)
                    var.ui.tabClientes.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index+=1

        except Exception as error:
            print('Problemas al mostrar tabla clientes',error)

    def oneCli(dni):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select direccion, provincia, municipio, sexo, envio from clientes where dni = :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(5):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas cargar datos cliente', error)

    def oneArticulo(codigo):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio where codigo = :codigo')
            query.bindValue(':codigo', codigo)
            if query.exec_():
                while query.next():
                    for i in range(3):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas cargar datos cliente', error)


    def cargaProv(self):
        try:
            prov = [""]
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT provincia FROM provincias')
            if query.exec_():
                while query.next():
                    prov.append(query.value(0))
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en módulo cargar provincias', error)


    def cargaMuni(self):
        try:
            id = 0
            var.ui.cmbMuni.clear()
            query = QtSql.QSqlQuery()
            prov = var.ui.cmbProv.currentText()
            query.prepare('SELECT id FROM provincias where provincia = :prov')
            query.bindValue(':prov',str(prov))
            if query.exec_():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('SELECT municipio FROM municipios where provincia_id = :id')
            query1.bindValue(':id',int(id))
            if query1.exec_():
                var.ui.cmbMuni.addItem('')
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))
        except Exception as error:
            print('Problemas al cargar municipios', error)

    def modifCli(modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'UPDATE clientes SET alta = :alta,apellidos = :apellidos,nombre = :nombre,direccion = :direccion,provincia= :provincia,municipio = :municipio, sexo = :sexo,pago = :pago, envio = :envio where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            query.bindValue(':envio', int(modcliente[9]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de cliente')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas modificar clientes. ', error)

    '''
    Módulos gestión base datos articulos
    '''

    def cargarTablaArt(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codigo, nombre, precio FROM articulos')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabArt.setRowCount(index+1)
                    var.ui.tabArt.setItem(index, 0,QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabArt.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArt.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio)))
                    index+=1

        except Exception as error:
            print('Problemas al mostrar tabla artículos',error)

    def altaArticulo(nuevoArt):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into articulos (nombre, precio) VALUES (:nombre, :precio)')
            query.bindValue(':nombre', str(nuevoArt[0]))
            query.bindValue(':precio', str(nuevoArt[1]))

            if query.exec_():
                print('Inserción de artículo correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo guardado con éxito')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Problemas guardado artículo',error)


    def bajaArticulo(codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM articulos WHERE codigo = :codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                print('Baja correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja articulo en conexion ', error)

    # def modifArt(modArt):
    #     try:
    #         query = QtSql.QSqlQuery()
    #         query.prepare(
    #             'UPDATE articulos SET nombre = :nombre,precio = :precio where codigo = :codigo')
    #         query.bindValue(':codigo', str(modArt[0]))
    #         query.bindValue(':nombre', str(modArt[1]))
    #         query.bindValue(':precio', str(modArt[2]))
    #         if query.exec_():
    #             print('Modificacion correcta')
    #             msg = QtWidgets.QMessageBox()
    #             msg.setWindowTitle('Información')
    #             msg.setIcon(QtWidgets.QMessageBox.Information)
    #             msg.setText('Datos modificados de producto')
    #             msg.exec()
    #         else:
    #             print('Error. ', query.lastError().text())
    #             msg = QtWidgets.QMessageBox()
    #             msg.setWindowTitle('Aviso')
    #             msg.setIcon(QtWidgets.QMessageBox.Warning)
    #             msg.setText(query.lastError().text())
    #             msg.exec()
    #
    #     except Exception as error:
    #         print('Problemas modificar producto. ', error)

    def modifArt(modArt):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre =:nombre, precio = :precio where codigo = :cod')
            query.bindValue(':cod', int(modArt[0]))
            query.bindValue(':nombre', str(modArt[1]))
            modArt[2] = [2].replace('€', '')
            modArt[2] = modArt[2].replace(',', '.')
            modArt[2] = float(modArt[2])
            modArt[2] = round(modArt[2], 2)
            modArt[2] = str(modArt[2])
            modArt[2] = locale.currency(float(modArt[2]))
            query.bindValue(':precio', str(modArt[2]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de Producto')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error modificar producto en conexion: ', error)

    def buscaClifac(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select dni,apellidos,nombre from clientes where dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    registro.append(query.value(1))
                    registro.append(query.value(2))
            return registro
        except Exception as error:
            print('Error en conexión buscar cliente. ', error)

    def altaFac(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (dni,fechafac) VALUES (:dni,:fecha)')
            query.bindValue(':dni', str(registro[0]))
            query.bindValue(':fecha', str(registro[1]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de alta.')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en conexión alta factura. ', error)

    def bajaFac(codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM facturas WHERE codfac = :codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                print('Baja correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura eliminada')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error al eliminar factura ',error)

    def cargaTabfacturas(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codfac, fechafac FROM facturas order by fechafac desc')
            if query.exec_():
                while query.next():
                    codfac = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    iconpapelera = QtGui.QPixmap("img/icon-papelera.png")
                    var.btnfacdel.setFixedSize(26,26)
                    var.btnfacdel.setIcon(QtGui.QIcon(iconpapelera))
                    var.ui.tabFacturas.setRowCount(index + 1)
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codfac)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.setContentsMargins(0,0,0,0)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    var.ui.tabFacturas.setCellWidget(index, 2,cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print('Error en cargar Tab Facturas', error)