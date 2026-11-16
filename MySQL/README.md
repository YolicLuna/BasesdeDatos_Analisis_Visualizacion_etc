# Ejercicios de MySQL - Prácticas

Esta sección contiene una colección de ejercicios prácticos de SQL con MySQL para desarrollar habilidades en gestión de bases de datos, consultas avanzadas y análisis de datos.

## Archivos del Repositorio

### 1. **Analisis_con_MySQL.sql**
**Objetivo:** Práctica de creación y manipulación de bases de datos educativas.

Este archivo contiene:
- Creación de una base de datos llamada `Alumnos_titulados` con dos tablas relacionadas
- Tabla `info_titulados`: Almacena información de estudiantes egresados (universidad, estado, carrera, promedio, fechas)
- Tabla `alumnos`: Contiene datos personales de los alumnos (nombre, edad, teléfono, email, dirección)
- **50 registros de ejemplo** con datos de universidades mexicanas y estudiantes de diferentes carreras
- Implementación de relaciones mediante **llaves foráneas** (Foreign Keys)

**Habilidades practicadas:** Creación de tablas, inserción de datos masivos, integridad referencial, relaciones uno-a-muchos.

---

### 2. **caso_practico.sql**
**Objetivo:** Análisis de datos e inteligencia de negocios para una tienda.

Este archivo presenta un caso de estudio real donde se actúa como analista de datos con consultas SQL enfocadas en:
- **Clientes más valiosos:** Identificar los 5 clientes con mayor volumen de compras
- **Productividad de empleados:** Determinar qué empleado ha generado más ventas
- **Productos populares:** Conocer los 3 productos más vendidos por cantidad
- **Análisis de proveedores:** Identificar proveedores con productos más vendidos
- **Análisis temporal:** Detectar la temporada de mayores ventas
- **Fidelización:** Calcular frecuencia de compras y gasto promedio por cliente

**Habilidades practicadas:** JOINs múltiples, GROUP BY, agregación (SUM, COUNT, AVG), LIMIT, ORDER BY, análisis de negocio.

---

### 3. **Pixar/** *(Carpeta)*
**Objetivo:** Carga de datos desde archivos CSV e importación de información externa.

Esta carpeta contiene:
- **Pixar.sql:** Script SQL que demuestra:
  - Creación de base de datos `Practicas` con tabla `Pixar`
  - **Importación de datos CSV** con el comando `LOAD DATA INFILE` desde `pixar_films.csv`
  - Manejo de valores nulos y conversión de datos (NULLIF)
  - Consultas prácticas sobre la tabla:
    - Filtrado por rango de duración (BETWEEN)
    - Ordenamiento y limitación de resultados (ORDER BY, LIMIT)
    - Búsqueda de texto con patrones (LIKE)
    - Uso de funciones de agrupación (COUNT, GROUP BY)
    - Validación de existencia de registros (IF EXISTS)

- **pixar_films.csv:** Archivo con datos reales de películas de Pixar (id, film, release_date, runtime, film_rating)

**Habilidades practicadas:** Carga de datos, importación CSV, valores nulos, filtrado avanzado, búsqueda de patrones, funciones condicionales.

---

### 4. **sql_Riaz.sql**
**Objetivo:** Modelado completo de base de datos para gestión de inventario y ventas.

Este archivo contiene un **modelo de base de datos integral** para una empresa de alimentos congelados:
- **Tabla Empleados:** Gestión de personal con datos de contacto
- **Tabla Clientes:** Información de clientes y direcciones
- **Tabla Proveedores:** Base de datos de proveedores
- **Tabla Productos:** Catálogo con precios de compra y venta
- **Tabla Ventas:** Registro de transacciones con múltiples campos
- **Tabla Pedidos:** Seguimiento de órdenes y entregas
- **Tabla Inventario:** Control de stock y gestión de almacén
- Implementación de **múltiples relaciones** entre tablas mediante llaves foráneas
- **Importación de datos CSV** desde múltiples archivos

**Habilidades practicadas:** Diseño relacional completo, integridad referencial, modelos de negocio reales, importación de datos en bloque, normalización de datos.

---

## Requisitos

- MySQL 5.7 o superior
- Cliente de MySQL (mysql command line, MySQL Workbench, etc.)

## Cómo usar estos archivos

1. Abre tu cliente de MySQL
2. Ejecuta cada archivo SQL según el orden que desees
3. Para los archivos en subcarpetas (ej: `Pixar/`), navega a esa carpeta o ajusta las rutas según sea necesario
4. Modifica las consultas y experimenta con diferentes condiciones
5. Intenta crear tus propias consultas basadas en los modelos presentados

## Recomendaciones de estudio

- Comienza con `Analisis_con_MySQL.sql` para entender relaciones básicas
- Continúa con `Pixar/Pixar.sql` para practicar importación y filtrado
- Usa `caso_practico.sql` para aprender análisis de datos
- Finaliza con `sql_Riaz.sql` para ver un modelo de negocio completo
