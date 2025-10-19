/*Caso práctico: "Optimización de operaciones y rendimiento"
Introducción:
Eres un analista de datos contratado por una tienda que busca optimizar sus operaciones, entender mejor a sus clientes 
y empleados, y maximizar las ventas y la gestión del inventario. La base de datos contiene información clave de clientes, 
empleados, inventario, pedidos, productos, proveedores y ventas.
Tu tarea es responder a las siguientes preguntas mediante consultas MySQL para extraer insights valiosos y 
apoyar las decisiones estratégicas.
*/

/*Clientes mas valiosos:
¿Quienes son los 5 clientes que mas han comprado?
*/

SELECT Clientes.Nombre, SUM(precio_total) AS total_compras
FROM Ventas
JOIN Clientes ON Ventas.cliente = Clientes.id_cliente
GROUP BY Clientes.Nombre
ORDER BY total_compras DESC
LIMIT 5;

/*Productividad de los empleados:
¿Qué empleado ha generado más ventas?
*/

SELECT Empleados.Nombre, SUM(precio_total) AS total_ventas
FROM Ventas
JOIN Empleados ON Ventas.empleado = Empleados.id_empleado
GROUP BY Empleados.Nombre
ORDER BY total_ventas DESC
LIMIT 3;


/*Productos mas populares:
¿Cuales son los 3 productos más vendidos por cantidad?
*/

SELECT Productos.producto, SUM(cantidad_producto) AS total_vendido
FROM Ventas
JOIN Productos ON Ventas.producto = Productos.id_producto
GROUP BY Productos.producto
ORDER BY total_vendido DESC
LIMIT 3;


/*Analisis de proveedores:
¿Cúales son los 3 proveedores tieneN los productos más vendidos?
*/

SELECT Proveedores.Nombre, Productos.producto, SUM(cantidad_producto) AS total_vendido
FROM Ventas
JOIN Productos ON Ventas.producto = Productos.id_producto
JOIN Proveedores ON Productos.proveedor = Proveedores.id_proveedor
GROUP BY Proveedores.Nombre, Productos.producto
ORDER BY total_vendido DESC
LIMIT 3

/*Temporada mas alta:
¿En que mes se registraron más ventas?
*/

SELECT DATE_FORMAT(fecha, '%Y-%m') AS mes, SUM(precio_total) AS total_ventas
FROM Ventas
WHERE fecha IS NOT NULL AND precio_total IS NOT NULL 
GROUP BY mes
ORDER BY total_ventas DESC
LIMIT 1;

/*Fidelidad de clientes:
¿Cuántas compras ha realizado cada cliente y cuál es el promedio de gasto por compra?
*/

SELECT Clientes.Nombre, COUNT(Ventas.id_venta) AS total_compras, AVG(precio_total) AS promedio_gasto
FROM Ventas
JOIN Clientes ON Ventas.cliente = Clientes.id_cliente
GROUP BY Clientes.Nombre
ORDER BY total_compras DESC
LIMIT 5;

