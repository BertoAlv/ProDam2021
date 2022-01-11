import conexion
import var
import ventana

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
        except Exception as error:
            print('Error en alta facturas. ',error)

    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblNumfac,var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            print(row)
            for i, dato in enumerate(datos):
                dato.setText(row[i])
        except Exception as error:
            print('Error en cargar los datos del articulo', error)