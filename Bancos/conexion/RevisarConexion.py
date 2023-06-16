import pyodbc

try:
    servidor = 'ADRIAN_JIMENEZ'
    baseDatos = 'Banco'

    conexion = pyodbc.connect('Driver={SQL Server};Server=ADRIAN_JIMENEZ;Database=Banco;Trusted_Connection=yes;')
    print('conexion exitosa')
    objconexion = conexion.cursor()
    objconexion.execute('SELECT * from Clientes')

    for ren in objconexion:
        print (ren)

except pyodbc.Error as e:
    print("Error de conexión")
    print(e)