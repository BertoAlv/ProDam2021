import os, var

from reportlab.pdfgen import canvas

class Informes():

    def listadoClientes(self):
        try:
            var.cv = canvas.Canvas('informes/listadoclientes.pdf')
            Informes.cabecera(self) #MAXIMO 595 ANCHO, 845 ALTO
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de Administración')
            var.cv.save()
            rootPath = '.\\informes'
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error en listar clientes ',error)

    def cabecera(self):
        try:
            logo = '.\\img\\logo-empresa.png'
            var.cv.setFont('Helvetica-Bold',14)
            var.cv.line(30,805,550,805)
            var.cv.line(30,710,550,710)
            var.cv.drawString(40,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica',11)
            var.cv.drawString(40,770,'CIF:111111111')
            var.cv.drawString(40,755,'Dirección: Avenida Galicia, 101')
            var.cv.drawString(40,740,'Vigo - 36216 - Spain')
            var.cv.drawString(40,725,'email: micorreo@gmail.com')
            var.cv.drawImage(logo,400,715)
        except Exception as error:
            print('Error en la cabecera ',error)