from PyQt5.QtSql import QSqlDatabase


class Conexion(object):
    __database = None

    def __init__(self):
        if Conexion.__database!=None:
            raise Exception("Ya existe una conexión")
        else:
            servidor = 'ADRIAN_JIMENEZ'  # Servidor al que se conectará
            baseDatos = 'Banco'  # Base de Datos
            Conexion.__database = QSqlDatabase.addDatabase("QODBC3")
            Conexion.__database.setDatabaseName('Driver={SQL Server};'
                                                'Server=' + servidor + ';'
                                                'Database=' + baseDatos + ';'
                                                'Trusted_Connection=yes;'
                                                )

    @staticmethod
    def cerrarConexion():
        if Conexion.__database.isOpen():
            Conexion.__database.close()

    @staticmethod
    def __validaEstatusConexion():
        if not Conexion.__database.isOpen():
            Conexion.__database.open()

    @staticmethod
    def getConexion():
        if Conexion.__database == None:
            Conexion()
            Conexion.__validaEstatusConexion()
        return Conexion.__database