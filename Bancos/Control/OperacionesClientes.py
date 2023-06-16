from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QSqlQueryModel
from PyQt5.QtSql import QSqlQuery
from conexion.Conexion import Conexion

class OperacionesClientes:

    def actualizar(self, parametros):
        try:
            band = True
            self.conexion = Conexion.getConexion()  # Abrir conexión
            query = QSqlQuery(self.conexion)  # Creamos un objeto de la colección que ejecuta la sentencia SQL
            self.conexion.database().transaction()  # Preparar la base de datos para la inserción
            sql = 'UPDATE Clientes SET nombre = :nombre, apellidos = :apellidos, tipo = :tipo, saldo = :saldo, credito = :credito WHERE IDcliente = :IDcliente'
            query.prepare(sql)
            query.bindValue(':IDcliente', parametros.get('IDcliente'))
            query.bindValue(':nombre', parametros.get('nombre'))
            query.bindValue(':apellidos', parametros.get('apellidos'))
            query.bindValue(':tipo', parametros.get('tipo'))
            query.bindValue(':saldo', parametros.get('saldo'))
            query.bindValue(':credito', parametros.get('credito'))
            query.exec()
            self.conexion.database().commit()
            return band
        except Exception as ex:
            QMessageBox.critical(None, 'Error', ex.__str__())
            return False


    def consultarTodos(self, interfazGrafica):
        try:
            band = True
            modelo=QSqlQueryModel()#genera un modelo sql
            self.conexion=Conexion.getConexion()
            sql = 'select * from Clientes'
            modelo.setQuery(sql, self.conexion)
            interfazGrafica.tblClientes.setModel(modelo)
        except Exception as ex:
            band = False
            QMessageBox.critical(self, 'Error', ex.__str__())

        return band

    def consultarUno(self, interfazGrafica, cadena):
        try:
            band = True
            modelo = QSqlQueryModel()#genera un modelo sql
            self.conexion = Conexion.getConexion()
            sql = 'select * from Clientes where IDcliente=' + cadena
            #modelo.bindValue(':Banco', Banco)
            modelo.setQuery(sql, self.conexion)
            interfazGrafica.tblClientes.setModel(modelo)
        except Exception as ex:
            band = False
            QMessageBox.critical(self, 'Error', ex.__str__())

        return band

    def insertar(self, parametros):
        try:
            band = True
            self.conexion = Conexion.getConexion()  # Abrir conexión
            query = QSqlQuery(self.conexion)  # Creamos un objeto de la colección que ejecuta la sentencia SQL
            self.conexion.database().transaction()  # Preparar la base de datos para la inserción

            # Validar si el IDcliente ya existe en la base de datos
            id_cliente = parametros.get('IDcliente')
            existe_query = QSqlQuery(self.conexion)
            existe_query.prepare('SELECT COUNT(*) FROM Clientes WHERE IDcliente = :id_cliente')
            existe_query.bindValue(':id_cliente', id_cliente)
            existe_query.exec()

            if existe_query.next() and existe_query.value(0) > 0:
                # El IDcliente ya existe, mostrar mensaje de error
                QMessageBox.information(None, 'Información', 'Cliente existente')
                band = False
            else:
                # El IDcliente no existe, realizar la inserción
                sql = 'INSERT INTO Clientes (IDcliente, nombre, apellidos, tipo, saldo, credito) ' \
                      'VALUES (:IDcliente, :nombre, :apellidos, :tipo, :saldo, :credito)'
                query.prepare(sql)
                query.bindValue(':IDcliente', parametros.get('IDcliente'))
                query.bindValue(':nombre', parametros.get('nombre'))
                query.bindValue(':apellidos', parametros.get('apellidos'))
                query.bindValue(':tipo', parametros.get('tipo'))
                query.bindValue(':saldo', parametros.get('saldo'))
                query.bindValue(':credito', parametros.get('credito'))
                query.exec()
                self.conexion.database().commit()

            return band
        except Exception as ex:
            QMessageBox.critical(None, 'Error', ex.__str__())
            return False




    def eliminar(self, NoCliente):
        try:
            band = True
            self.conexion = Conexion.getConexion()
            query = QSqlQuery(self.conexion)
            self.conexion.database().transaction()
            sql = 'delete from Clientes where IDcliente = :NoCliente'
            query.prepare(sql)
            query.bindValue(':NoCliente', NoCliente)
            query.exec()  # Ejecuta la sentencia SQL
            self.conexion.database().commit()
        except Exception as ex:
            band = False
            QMessageBox.critical(self, ex.__str__())
        return band
