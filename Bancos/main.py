import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import QStandardItemModel

from Control.Control import Control_Clientes
from Control.OperacionesClientes import OperacionesClientes

class Main(QMainWindow):

    def __init__(self,parent=None):
        try:
            super(Main,self).__init__(parent)
            loadUi('assets/Ventana.ui',self)
            self.agregarTipo()
            self.eventos()
            self.objInterfazGrafica = OperacionesClientes()

        except Exception as ex:
            QMessageBox.critical(self,'ERROR',ex.__str__())

    def eventos(self):
        #eventos barra de herramientas
        self.actionSalir.triggered.connect(self.salir)
        self.psbRetirar.clicked.connect(lambda: Control_Clientes.Retirar(self))
        #Agregar usuario
        self.actionAgregar_2.triggered.connect(lambda: Control_Clientes.insertarAspirante(self))
        self.psbAgregar.clicked.connect(lambda: Control_Clientes.insertarAspirante(self))
        self.actionAgregar.triggered.connect(lambda: Control_Clientes.insertarAspirante(self))
        #eliminar usuario
        self.actionEliminar.triggered.connect(lambda: Control_Clientes.eliminarAspirante(self))
        self.actionEliminar_2.triggered.connect(lambda: Control_Clientes.eliminarAspirante(self))
        #actualizar
        self.actionActualizar.triggered.connect(lambda: Control_Clientes.Actualizar(self))
        self.actionActualizar_2.triggered.connect(lambda: Control_Clientes.Actualizar(self))
        self.psbAgregar_2.clicked.connect(lambda: Control_Clientes.Actualizar(self))
        #limpia controles
        self.actionNuevo.triggered.connect(lambda: Control_Clientes.limpiaControles(self))
        self.actionNuevo_2.triggered.connect(lambda: Control_Clientes.limpiaControles(self))
        #modifica Credito
        self.psbModificar.clicked.connect(self.modificaCredito)

        self.actionConsultar.triggered.connect(lambda: Control_Clientes.consultar(self))
        self.psbAbonar.clicked.connect(lambda: Control_Clientes.abonar(self))
        self.psbBuscar.clicked.connect(lambda: Control_Clientes.consultar(self))
        self.tblClientes.clicked.connect(lambda: Control_Clientes.seleccionAspirante(self))
        self.lneNoCuenta.textChanged.connect(self.ingresaNoCuenta)
        self.lneNombre.textChanged.connect(self.ingresaNombre)
        self.lneApellidos.textChanged.connect(self.ingresaApellidos)
        self.lneSaldo.textChanged.connect(self.ingresaSaldo)
        self.lneAbono.textChanged.connect(self.ingresaAbono)
        self.lneCredito.textChanged.connect(self.ingresaCredito)
        self.cmbTipoCuenta.currentTextChanged.connect(self.habilitarCredito)

#datos del alumno

    def ingresaNoCuenta(self):
        cadena = self.lneNoCuenta.text()
        if cadena.isdigit() or cadena == '':
            self.lneNoCuenta.setText(cadena)
        else:
            QMessageBox.information(self, 'Dato incorrecto', 'no es digito')
            self.lneNoCuenta.setText(cadena[:-1])

    def ingresaSaldo(self):
        cadena = self.lneSaldo.text()
        if cadena.replace('.', '', 1).isdigit() or cadena == '':
            self.lneSaldo.setText(cadena)
        else:
            QMessageBox.information(self, 'Dato incorrecto', 'no es digito')
            self.lneSaldo.setText(cadena[:-1])

    def ingresaCredito(self):
        cadena = self.lneCredito.text()
        if cadena.replace('.', '', 1).isdigit() or cadena == '':
            self.lneCredito.setText(cadena)
        else:
            QMessageBox.information(self, 'Dato incorrecto', 'no es digito')
            self.lneCredito.setText(cadena[:-1])

    def ingresaAbono(self):
        cadena = self.lneAbono.text()
        if cadena.replace('.', '', 1).isdigit() or cadena == '':
            self.lneAbono.setText(cadena)
        else:
            QMessageBox.information(self, 'Dato incorrecto', 'no es digito')
            self.lneAbono.setText(cadena[:-1])

    def ingresaNombre(self):
        self.lneNombre.setText(self.lneNombre.text().upper())

    def ingresaApellidos(self):
        self.lneApellidos.setText(self.lneApellidos.text().upper())

    def habilitarCredito(self):
        if (self.cmbTipoCuenta.currentText() == 'Debito'):
            self.psbModificar.setEnabled(False)
        elif (self.cmbTipoCuenta.currentText() == 'Credito'):
            if(self.lneNoCuenta.text() != "" and self.lneNombre.text() != "" and self.lneApellidos.text() != "" and self.lneSaldo.text() != ""):
                self.psbModificar.setEnabled(True)

    def modificaCredito(self):
        nuevoCredito = float(self.lneCreditoModificar.text())
        self.lneCredito.setText(str(nuevoCredito))



#datos
    def agregarTipo(self):
        Tipo = ['Debito', 'Credito']
        self.cmbTipoCuenta.addItems(Tipo)

    def salir(self):
        resultado = QMessageBox.question(self,'Salir','¿Está seguro de salir?',
                                       QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if resultado == QMessageBox.Yes:
            sys.exit(app.exec_())


if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana=Main()
    ventana.show()
    sys.exit(app.exec_())
