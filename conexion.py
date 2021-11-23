from PyQt5 import QtSql, QtWidgets

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

    # def altaCli2(newcli):
    #     try:
    #         query = QtSql.QSqlQuery()
    #         query.prepare('insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo) VALUES '
    #                       '(:dni, :apellidos, :nombre, :direccion, :provincia, :sexo)')
    #         query.bindValue(':dni', str(newcli[0]))
    #         query.bindValue(':apellidos', str(newcli[1]))
    #         query.bindValue(':nombre', str(newcli[2]))
    #         query.bindValue(':direccion', str(newcli[3]))
    #         query.bindValue(':provincia', str(newcli[4]))
    #         query.bindValue(':sexo', str(newcli[5]))
    #
    #         if query.exec_():
    #             pass
    #         else:
    #             msg = QtWidgets.QMessageBox()
    #             msg.setWindowTitle('Aviso')
    #             msg.setIcon(QtWidgets.QMessageBox.Warning)
    #             msg.setText(query.lastError().text())
    #             msg.exec()
    #     except Exception as error:
    #         print('Problemas alta cliente',error)

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