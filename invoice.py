import conexion
import var
import ventana
from PyQt5 import QtSql, QtWidgets, QtCore

class Facturas():

    def buscaCli(self):
        try:
            dni = var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro=conexion.Conexion.buscaClifac(dni)
            nombre=registro[0] + ','+registro[1]
            var.ui.txtClienteFac.setText(nombre)
        except Exception as error:
            print('Error al buscar cliente en facturas. ',error)

    def facturar(self):
        try:
            registro=[]
            dni=var.ui.txtDNIfac.text().upper()
            registro.append(str(dni))
            var.ui.txtDNIfac.setText(dni)
            fechafac=var.ui.txtFechaFac.text()
            registro.append(str(fechafac))
            conexion.Conexion.buscaClifac(dni)
            conexion.Conexion.altaFac(registro)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('Error en alta facturas. ',error)

    def bajaFac(self):
        try:
            codfac = var.ui.lblNumfac.text()
            conexion.Conexion.bajaFac(codfac)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('error baja',error)

    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblNumfac, var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            # Aquí cargamos el dni y nombre del cliente
            dni = conexion.Conexion.buscaDNIFac(row[0])
            var.ui.txtDNIfac.setText(str(dni))
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ',' + registro[1]
                var.ui.txtClienteFac.setText(nombre)
            Facturas.cargaLineaVenta(self)
        except Exception as error:
            print('Error al cargar factura. ', error)

    def cargaLineaVenta(self):
        try:
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbProducto(self)

            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index,3,var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)

    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            print(dato)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row,2).setTextAlignment(QtCore.Qt.AlignCenter)
            precio = dato[1].replace('€','')
            var.precio = precio.replace(',','.')

        except Exception as error:
            print('Error en proceso venta: ', error)

    def totalLineaVenta(self = None):
        try:
            row = var.ui.tabVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total_venta = round((float(var.precio) * float(cantidad)),2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_venta) + ' €'))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        except Exception as error:
            print('Error en el total linea venta', error)
