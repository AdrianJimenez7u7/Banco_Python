from PyQt5.QtWidgets import QMessageBox

class Control_Clientes:

    def consultar(self):
        try:
            if self.lneNoControlBuscar.text() == '': #consultar a todos los alumnos
                if not self.objInterfazGrafica.consultarTodos(self):
                    QMessageBox.critical(self, 'Informacion', 'ERROR No pudo Consultar a todos')

            else:   #consultar un solo alumno
                cadena = self.lneNoControlBuscar.text()
                if not self.objInterfazGrafica.consultarUno(self, cadena):
                    QMessageBox.critical(self, 'Informacion', f'no puedo consulta {cadena}')

        except Exception as ex:
            QMessageBox.critical(self, 'Error', ex.__str__())

    def abonar(self):
        try:
            saldo_actual = float(self.lneSaldo.text())
            abono = float(self.lneAbono.text())
            nuevo_saldo = saldo_actual + abono
            self.lneSaldo.setText(str(nuevo_saldo))
            self.lneAbono.clear()
        except Exception as ex:
            QMessageBox.critical(self, 'Error', ex.__str__())

    def Retirar(self):
        saldo_actual = float(self.lneSaldo.text())
        retiro = float(self.lneRetirar.text())
        credito = float(self.lneCredito.text())
        if(self.cmbTipoCuenta.currentText() == 'Debito'):
            if(saldo_actual >= retiro):
                self.lneSaldo.setText(str(saldo_actual - retiro))
                self.lneRetirar.clear()
            else:
                QMessageBox.information(None, 'Información', 'Saldo Insuficiente')
                self.lneRetirar.clear()
        elif(self.cmbTipoCuenta.currentText() == 'Credito'):
            if(saldo_actual >= retiro):
                self.lneSaldo.setText(str(saldo_actual - retiro))
                self.lneRetirar.clear()
            elif(retiro <= (saldo_actual + credito)):
                retiro = (retiro - saldo_actual)
                saldo_actual = 0;
                self.lneSaldo.setText(str(saldo_actual))
                credito = (credito - retiro)
                retiro = 0
                self.lneCredito.setText(str(credito))
                self.lneRetirar.clear()
            elif(retiro > (saldo_actual + credito)):
                QMessageBox.information(None, 'Información', 'Saldo y Credito Insuficiente')
        self.lneRetirar.clear()

    def limpiaControles(self):
        try:
            self.lneNoCuenta.clear()
            self.lneNoCuenta.setReadOnly(False)
            self.lneNoControlBuscar.clear()
            self.lneAbono.clear()
            self.lneAbono.setReadOnly(True)
            self.lneRetirar.clear()
            self.lneRetirar.setReadOnly(True)
            self.lneCreditoModificar.clear()
            self.lneCreditoModificar.setReadOnly(True)
            self.lneNombre.clear()
            self.lneApellidos.clear()
            self.lneSaldo.clear()
            self.lneSaldo.setReadOnly(False)
            self.lneCredito.clear()
            self.lneCredito.setReadOnly(False)
            self.cmbTipoCuenta.setCurrentIndex(0)
            self.psbModificar.setEnabled(False)
            self.psbRetirar.setEnabled(False)
            self.psbAbonar.setEnabled(False)
            self.psbAgregar_2.setEnabled(False)
        except Exception as ex:
            QMessageBox.critical(self, 'ERROR', ex.__str__())

    def seleccionAspirante(self):
        try:
            indices = self.tblClientes.selectionModel().selectedIndexes()
            modelo = self.tblClientes.model()
            for indice in sorted(indices):
                ind = indice.row()
                self.lneNoCuenta.setText(modelo.data(modelo.index(ind, 0)))
                self.lneNombre.setText(modelo.data(modelo.index(ind, 1)))
                self.lneApellidos.setText(modelo.data(modelo.index(ind, 2)))
                self.cmbTipoCuenta.setCurrentText(modelo.data(modelo.index(ind, 3)))
                self.lneSaldo.setText(str(float(modelo.data(modelo.index(ind, 4)))))
                self.lneCredito.setText(str(float(modelo.data(modelo.index(ind, 5)))))
                self.lneNoCuenta.setReadOnly(True)
                self.lneSaldo.setReadOnly(True)
                self.lneCredito.setReadOnly(True)
                self.lneCreditoModificar.setReadOnly(False)
                self.lneRetirar.setReadOnly(False)
                self.lneAbono.setReadOnly(False)
                self.psbModificar.setEnabled(True)
                self.psbRetirar.setEnabled(True)
                self.psbAbonar.setEnabled(True)
                self.psbAgregar_2.setEnabled(True)
        except Exception as ex:
            QMessageBox.critical(self, 'ERROR', ex.__str__())

    def insertarAspirante(self):
        try:
            parametros = {
                'IDcliente':self.lneNoCuenta.text(),
                'nombre':self.lneNombre.text(),
                'apellidos':self.lneApellidos.text(),
                'tipo':self.cmbTipoCuenta.currentText(),
                'saldo':self.lneSaldo.text(),
                'credito':self.lneCredito.text()
            }

            if self.objInterfazGrafica.insertar(parametros):
                QMessageBox.critical(self, 'Informacion', 'Datos del aspirante insertado correctamente')
                Control_Clientes.limpiaControles(self)
            else:
                QMessageBox.critical(self, 'Informacion', f'datos no insertados')
        except Exception as ex:
            QMessageBox.critical(self, 'ERROR', ex.__str__())

    def Actualizar(self):
        try:
            parametros = {
                'IDcliente':self.lneNoCuenta.text(),
                'nombre':self.lneNombre.text(),
                'apellidos':self.lneApellidos.text(),
                'tipo':self.cmbTipoCuenta.currentText(),
                'saldo':self.lneSaldo.text(),
                'credito':self.lneCredito.text(),
            }

            if self.objInterfazGrafica.actualizar(parametros):
                QMessageBox.critical(self, 'Informacion', 'Datos del Cliente Actualizados correctamente')
                Control_Clientes.limpiaControles(self)
            else:
                QMessageBox.critical(self, 'Informacion', f'datos no Actualizados')
        except Exception as ex:
            QMessageBox.critical(self, 'ERROR', ex.__str__())

    def eliminarAspirante(self):
        try:
            self.Cliente = self.lneNoCuenta.text()
            resultado = QMessageBox.question(self,'ELIMINAR', f'¿estas seguro de eliminar a {self.Cliente}?', QMessageBox.Yes|QMessageBox.No)
            if resultado == QMessageBox.Yes:
                if self.objInterfazGrafica.eliminar(self.Cliente):
                    QMessageBox.critical(self, 'Informacion', 'Datos del Cliente eliminado correctamente')
                    Control_Clientes.limpiaControles(self)
                else:
                    QMessageBox.critical(self, 'Informacion', f'datos no eliminado')

        except Exception as ex:
            QMessageBox.critical(self, 'ERROR', ex.__str__())