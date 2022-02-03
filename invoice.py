import conexion
import eventos
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


    def cargaCliFac(self):
        # carga datos de cliente en Facturación al seleccionar en tabla Clientes
        try:
            fila = var.ui.tabClientes.selectedItems() #seleccionamos fila en tab clientes
            datos = [var.ui.txtDNIfac, var.ui.txtClienteFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i]) #cargamos los datos en las cajas de texto
            '''carga el dni y los apellidos, falta nombre'''

        except Exception as error:
            print("Error en cargar datos de un cliente en Facturación", error)

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
            codfac = conexion.Conexion.buscaCodFac(self)
            var.ui.lblNumfac.setText(str(codfac))
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
            conexion.Conexion.cargarLineasVenta(str(var.ui.lblNumfac.text()))
        except Exception as error:
            print('Error al cargar factura. ', error)

    def cargaLineaVenta(index):
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.currentIndexChanged.connect(Facturas.procesoVenta)
            conexion.Conexion.cargarCmbProducto(self=None)
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)

    def procesoVenta(self):
        try:
            dato = []
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            var.codpro = dato[0]
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row,2).setTextAlignment(QtCore.Qt.AlignCenter)
            precio = dato[1].replace('€','')
            var.precio = precio.replace(',','.')
        except Exception as error:
            print('Error en proceso venta: ', error)

    def totalLineaVenta(self = None):
        try:
            venta = []
            row = var.ui.tabVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total_venta = round((float(var.precio) * float(cantidad)),2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_venta) + ' €'))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignCenter)
            codfac = var.ui.lblNumfac.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(var.precio))
            venta.append(float(cantidad))
            conexion.Conexion.cargarVenta(venta)
            conexion.Conexion.cargarLineasVenta(codfac)
        except Exception as error:
            print('Error en el total linea venta', error)

    def limpiaFormFac(self):
        try:
            cajas = [var.ui.txtDNIfac, var.ui.lblNumfac, var.ui.txtFechaFac, var.ui.txtClienteFac]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error al limpiar formulario facturación', error)
