DROP DATABASE Alimentos_congelados;
CREATE DATABASE Alimentos_congelados;

USE Alimentos_congelados;

CREATE TABLE Empleados(
id_empleado VARCHAR(20) UNIQUE PRIMARY KEY,
Nombre VARCHAR(100),
Puesto VARCHAR(50),
Telefono VARCHAR(20),
Correo VARCHAR(50),
Direccion VARCHAR(100)
);

CREATE TABLE Clientes(
id_cliente VARCHAR(20) UNIQUE PRIMARY KEY,
Nombre VARCHAR(100),
Telefono VARCHAR(20),
Correo VARCHAR(50),
Direccion VARCHAR(100)
);

CREATE TABLE Proveedores(
id_proveedor VARCHAR(20) UNIQUE PRIMARY KEY,
Nombre VARCHAR(100),
Telefono VARCHAR(20),
Correo VARCHAR(50),
Direccion VARCHAR(100)
);

CREATE TABLE Productos(
id_producto VARCHAR(20) UNIQUE PRIMARY KEY,
producto VARCHAR(100),
descripcion VARCHAR(100),
categoria VARCHAR(50),
proveedor VARCHAR(50),
FOREIGN KEY (proveedor) REFERENCES Proveedores(id_proveedor),
precio_de_compra DECIMAL(10,2),
precio_de_venta DECIMAL(10,2)
); 

CREATE TABLE Ventas(
id_venta VARCHAR(20) UNIQUE PRIMARY KEY,
empleado VARCHAR(100),
FOREIGN KEY (empleado) REFERENCES Empleados(id_empleado),
producto VARCHAR(100),
FOREIGN KEY (producto) REFERENCES Productos(id_producto),
cliente VARCHAR(50),
FOREIGN KEY (cliente) REFERENCES Clientes(id_cliente),
fecha DATE,
cantidad_producto DECIMAL(10,2),
precio_de_venta DECIMAL(10,2),
precio_total DECIMAL(10,2),
metodo_de_pago VARCHAR(50),
canal_de_venta VARCHAR(50)
);

CREATE TABLE Pedidos(
id_pedido VARCHAR(20) UNIQUE PRIMARY KEY,
empleado VARCHAR(100),
FOREIGN KEY (empleado) REFERENCES Empleados(id_empleado),
cliente VARCHAR(50),
FOREIGN KEY (cliente) REFERENCES Clientes(id_cliente),
producto VARCHAR(100),
FOREIGN KEY (producto) REFERENCES Productos(id_producto),
fecha_pedido DATE,
fecha_entrega_estimada DATE,
estado_pedido VARCHAR(20)
);

CREATE TABLE Inventario(
producto VARCHAR(100),
FOREIGN KEY (producto) REFERENCES Productos(id_producto),
proveedor VARCHAR(50),
FOREIGN KEY (proveedor) REFERENCES Proveedores(id_proveedor),
categoria VARCHAR(50),
cantidad_existente DECIMAL(10,2),
stock_minimo DECIMAL(10,2),
ultima_actualizacion DATE,
estatus VARCHAR(20)
);

# Cargar datos desde archivos CSV

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/Clientes.csv'
INTO TABLE Clientes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/Proveedores.csv'
INTO TABLE Proveedores
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/productos.csv'
INTO TABLE Productos
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/ventas.csv'
INTO TABLE Ventas
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
