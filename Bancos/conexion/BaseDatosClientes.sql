CREATE DATABASE Banco;
USE  Banco

CREATE TABLE Clientes (
  IDcliente VARCHAR(8) PRIMARY KEY NOT NULL,
  nombre VARCHAR(80) NOT NULL,
  apellidos VARCHAR(80) NOT NULL,
  tipo VARCHAR(20) NOT NULL,
  saldo DECIMAL(20, 2),
  credito DECIMAL(20, 2)
);
INSERT INTO Clientes VALUES ('00000001', 'Adrian', 'Jimenez', 'Debito', 8000.80, null);
INSERT INTO Clientes VALUES ('00000002', 'Juan', 'González', 'Credito', 15000.50, 5000.25);
INSERT INTO Clientes VALUES ('00000003', 'María', 'López', 'Credito', 20000.75, 10000.50);
INSERT INTO Clientes VALUES ('00000004', 'Pedro', 'Martínez', 'Credito', 12000.00, 0);
INSERT INTO Clientes VALUES ('00000005', 'Laura', 'Rodríguez', 'Credito', 5000.25, 2500.10);
INSERT INTO Clientes VALUES ('00000006', 'Carlos', 'Gómez', 'Credito', 8000.80, 0);
INSERT INTO Clientes VALUES ('00000007', 'Ana', 'Sánchez', 'Credito', 100000.00, 50000.00);

SELECT * FROM Clientes;