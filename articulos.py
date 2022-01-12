import conexion
import eventos
import var
from ventana import *
import locale
locale.setlocale( locale.LC_ALL, '' )

class Articulos():

    def altaArt(self):
        try:
            registro = []
            producto = var.ui.txtNomeArt.text()
            producto = producto.title()
            registro.append(producto)
            precio = var.ui.txtPrecio.text()
            precio = precio.replace(',', '.') #necesita estar con punto como en américa
            precio = locale.currency(float(precio))
            registro.append(precio)
            conexion.Conexion.altaArticulo(registro)
            conexion.Conexion.cargarTablaArt(self)

        except Exception as error:
            print('Error en alta productos: ', error)

    def cargaArticulo(self):
        try:
            fila = var.ui.tabArt.selectedItems()
            datos = [var.ui.lblCodArt,var.ui.txtNomeArt, var.ui.txtPrecio]
            if fila:
                row = [dato.text() for dato in fila]
            print(row)
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            registro = conexion.Conexion.oneArticulo(row[0])
        except Exception as error:
            print('Error en cargar los datos del articulo', error)


    def limpiaFormArt(self):
        try:
            cajas = [var.ui.lblCodArt, var.ui.txtNomeArt, var.ui.txtPrecio]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error limpiar formulario Articulos', error)

    def modifArt(self):
        try:
            modArt = []
            articulo = [var.ui.lblCodArt, var.ui.txtNomeArt, var.ui.txtPrecio]
            for i in articulo:
                modArt.append(i.text())
            conexion.Conexion.modifArt(modArt)
            conexion.Conexion.cargarTabCli(self)
        except Exception as error:
            print('Error en modificar articulo. ', error)

    def bajaArt(self):
        try:
            codigo = var.ui.txtCodArt.text()
            conexion.Conexion.bajaArticulo(codigo)
            conexion.Conexion.cargarTablaArt(self)
        except Exception as error:
            print('Error en eliminar articulo ',error)
