# 💪 Ejercicios Prácticos

Esta carpeta contiene ejercicios y prácticas para aplicar los conocimientos adquiridos en las diferentes tecnologías estudiadas.

## 🎯 Propósito

- Aplicar conceptos teóricos en situaciones prácticas
- Reforzar el aprendizaje mediante ejercicios resueltos
- Desarrollar habilidades de resolución de problemas
- Crear un portafolio de casos prácticos

## 📁 Contenido Actual

```
Ejercicios/
├── README.md
├── Analisis_con_MySQL.sql     # Ejercicios de análisis con MySQL
└── congelados_sql/           # Caso práctico de tienda de alimentos
    ├── sql_Riaz.sql          # Estructura de base de datos completa
    └── caso_practico_1.sql   # Análisis de optimización y rendimiento
```

---

## �️ **Ejercicios de MySQL**

**Archivo**: [`Analisis_con_MySQL.sql`](./Analisis_con_MySQL.sql)

### Descripción
Ejercicios prácticos aplicando conceptos de MySQL con una base de datos de estudiantes titulados que incluye:
- Tabla `info_titulados`: 101 registros con información académica
- Tabla `alumnos`: 101 registros con datos personales
- Relación mediante llave foránea para practicar JOINs

### Ejercicios Incluidos
- ✅ **Consultas básicas**: SELECT con filtros y condiciones
- ✅ **Agregaciones**: COUNT, SUM, AVG, MIN, MAX
- ✅ **Agrupamiento**: GROUP BY y HAVING
- ✅ **Joins**: INNER JOIN, LEFT JOIN con múltiples condiciones
- ✅ **Ordenamiento**: ORDER BY con criterios complejos
- ✅ **Análisis estadístico**: Promedios, rankings, distribuciones

### Casos de Análisis
- Estudiantes titulados por año y universidad
- Promedios académicos por carrera
- Distribución geográfica de universidades
- Rankings de mejores estudiantes
- Análisis de datos relacionales con JOINs

---

## 🏪 **Caso Práctico: Tienda de Alimentos Congelados**

**Carpeta**: [`congelados_sql/`](./congelados_sql/)

### Descripción
Caso práctico completo de una tienda de alimentos congelados que busca optimizar sus operaciones y maximizar las ventas. Incluye diseño de base de datos completa y análisis estratégico de negocio.

### **📄 sql_Riaz.sql** - Estructura de Base de Datos
**Base de datos completa** con 7 tablas relacionadas:

- **👥 Empleados**: Gestión de personal de la tienda
- **🛍️ Clientes**: Base de datos de clientes
- **🏭 Proveedores**: Información de proveedores
- **📦 Productos**: Catálogo completo con precios
- **💰 Ventas**: Registro de todas las transacciones
- **📋 Pedidos**: Gestión de pedidos y entregas
- **📊 Inventario**: Control de stock y existencias

### **📈 caso_practico_1.sql** - Análisis de Optimización
**6 análisis estratégicos** para la toma de decisiones:

- ✅ **Clientes más valiosos**: TOP 5 clientes por volumen de compras
- ✅ **Productividad empleados**: Ranking de empleados por ventas generadas
- ✅ **Productos populares**: TOP 3 productos más vendidos por cantidad
- ✅ **Análisis de proveedores**: Proveedores con productos más exitosos
- ✅ **Temporada alta**: Identificación del mes con mayor facturación
- ✅ **Fidelidad de clientes**: Frecuencia de compra y gasto promedio

### Características Técnicas
- **Relaciones complejas**: Foreign keys entre todas las tablas
- **Joins avanzados**: Consultas con múltiples tablas relacionadas
- **Agregaciones**: SUM, COUNT, AVG para análisis estadístico
- **Funciones de fecha**: DATE_FORMAT para análisis temporal
- **Optimización**: Consultas eficientes para grandes volúmenes de datos

### Casos de Uso Empresarial
- **Estrategia comercial**: Identificar clientes y productos clave
- **Gestión de inventario**: Optimizar stock basado en demanda
- **Recursos humanos**: Evaluar desempeño de empleados
- **Análisis temporal**: Planificar campañas según temporadas
- **Relaciones con proveedores**: Fortalecer alianzas estratégicas

---

## 📋 Próximos Ejercicios

### **Python - NumPy y Pandas** *(Planificado)*
- Manipulación de arrays multidimensionales
- Análisis exploratorio de datos (EDA)
- Limpieza y transformación de datasets
- Estadística descriptiva e inferencial

### **Proyectos Integrados** *(Planificado)*
- Análisis completo desde MySQL hasta Python
- Visualización de resultados
- Reportes automatizados

---

## � Metodología

1. **Problema definido**: Cada ejercicio tiene un objetivo claro
2. **Solución paso a paso**: Código comentado y explicado
3. **Validación**: Verificación de resultados
4. **Documentación**: Explicación del proceso y conclusiones

---

*Para apuntes teóricos consultar: [`MySQL/`](../MySQL/) y [`Analisis_Python/`](../Analisis_Python/)*