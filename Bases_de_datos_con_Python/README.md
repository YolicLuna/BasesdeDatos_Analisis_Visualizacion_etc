# Bases de Datos con Python – Proyectos y Ejemplos Prácticos

Este directorio contiene una colección completa de proyectos y ejemplos prácticos para trabajar con bases de datos usando Python. Incluye implementaciones con diferentes tecnologías: conectores nativos, ORMs, y interfaces gráficas, cubriendo tanto MySQL como PostgreSQL.

## 🗂️ Estructura del Proyecto

### **📁 crud.py** - CRUD con PostgreSQL y psycopg2
Implementación completa de operaciones CRUD usando PostgreSQL con el conector psycopg2.

- **main.py**: Sistema CRUD interactivo con menú de consola
  - ✅ Crear, listar, actualizar y eliminar usuarios
  - ✅ Decoradores para validación y limpieza de pantalla
  - ✅ Manejo de excepciones y transacciones
  - ✅ Variables de entorno con python-decouple

### **📁 dbpython.py** - MySQL con PyMySQL
Conexión directa a MySQL usando PyMySQL con ejemplos de operaciones básicas.

- **main.py**: Operaciones fundamentales de base de datos
  - ✅ Creación y eliminación de tablas
  - ✅ Inserción individual y masiva de registros
  - ✅ Consultas SELECT con filtros y ordenamiento
  - ✅ Operaciones UPDATE y DELETE
  - ✅ Manejo de errores y conexiones

### **📁 peewee.py** - ORM Peewee con MySQL
Implementación usando el ORM Peewee para simplificar las operaciones de base de datos.

- **actualizar.py**: Gestión de modelos y operaciones ORM
  - ✅ Definición de modelos con Peewee
  - ✅ Creación automática de tablas
  - ✅ Inserción de registros (individual, masiva)
  - ✅ Actualización de registros con ORM
  - ✅ Campos con validaciones y restricciones

### **📁 postgresql.py** - PostgreSQL Completo
Proyecto integral con PostgreSQL incluyendo interfaz gráfica y de consola.

- **main.py**: Sistema CRUD completo con GUI
  - ✅ Interfaz de consola y gráfica con Tkinter
  - ✅ Operaciones CRUD con decoradores avanzados
  - ✅ GUI dark theme profesional
  - ✅ Validación de existencia de usuarios
  - ✅ Variables de entorno locales

- **interface.py**: Interfaz gráfica independiente
  - ✅ GUI con Tkinter y ttk
  - ✅ Formularios para gestión de usuarios
  - ✅ Tabla dinámica para visualización
  - ✅ Integración con funciones del main.py

### **📁 sql/** - Archivos SQL de Soporte
Scripts SQL para configuración inicial de bases de datos.

### **📁 sql_al_orm.py** - Migración SQL a ORM
Ejemplos de conversión de consultas SQL tradicionales a sintaxis ORM.

- **main.py**: Comparativas SQL vs ORM
- **joins.py**: Implementación de JOINs con ORM
- **eliminar.py**: Operaciones de eliminación
- **actualizar.py**: Operaciones de actualización
- **llaves_foraneas.py**: Manejo de relaciones
- **acceso_relaciones.py**: Navegación entre modelos relacionados

### **📁 sqlalchemy.py** - SQLAlchemy ORM
Implementación completa con SQLAlchemy, el ORM más potente de Python.

- **main.py**: Configuración básica con carga de datos JSON
  - ✅ Definición de tablas con SQLAlchemy Core
  - ✅ Carga masiva de datos desde JSON
  - ✅ Transacciones con rollback automático
  - ✅ Conexión a PostgreSQL

- **connection.py**: Gestión de conexiones
- **ob_reg.py**: Mapeo objeto-relacional
- **llave_foranea.py**: Relaciones entre tablas
- **eliminar.py**: Eliminación de registros
- **condiciones.py**: Consultas con filtros complejos

## 🛠️ Tecnologías Utilizadas

### **Bases de Datos**
- **PostgreSQL**: Base de datos relacional avanzada
- **MySQL**: Sistema de gestión de bases de datos popular

### **Conectores y ORMs**
- **psycopg2-binary** (2.9.11): Conector PostgreSQL
- **PyMySQL** (1.1.2): Conector MySQL puro Python
- **peewee** (3.18.2): ORM ligero y expresivo
- **SQLAlchemy** (2.0.44): ORM completo y potente

### **Librerías de Apoyo**
- **python-decouple** (3.8): Gestión de variables de entorno
- **tkinter**: Interfaces gráficas nativas
- **json**: Manejo de datos JSON

## 🚀 Configuración y Uso

### **1. Instalar Dependencias**
```bash
pip install -r ../requirements.txt
```

### **2. Configurar Variables de Entorno**
Cada proyecto incluye su archivo `.env` correspondiente:

```bash
# Para PostgreSQL
DATABASE_URL=postgresql://usuario:password@localhost:5432/basedatos

# Para MySQL  
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=tu_password
MYSQL_DATABASE=python_db
```

### **3. Ejecutar Proyectos**
```bash
# CRUD PostgreSQL
python crud.py/main.py

# MySQL directo
python dbpython.py/main.py

# ORM Peewee
python peewee.py/actualizar.py

# PostgreSQL completo
python postgresql.py/main.py

# SQLAlchemy
python sqlalchemy.py/main.py
```

## 📚 Conceptos Aprendidos

### **Conexiones Directas**
- Manejo de cursores y transacciones
- Preparación de consultas parametrizadas
- Gestión de errores de conexión
- Pool de conexiones

### **ORMs (Object-Relational Mapping)**
- Definición de modelos y relaciones
- Migraciones automáticas de esquemas
- Consultas orientadas a objetos
- Lazy loading y eager loading

### **Interfaces de Usuario**
- Aplicaciones de consola interactivas
- GUIs con Tkinter
- Validación de formularios
- Actualización dinámica de datos

### **Buenas Prácticas**
- Separación de configuración y código
- Manejo seguro de credenciales
- Validación de entrada de datos
- Logging y manejo de errores

## 🎯 Casos de Uso

### **Para Aprendizaje**
- **Principiantes**: Empezar con `dbpython.py` (conexión directa)
- **Intermedios**: Explorar ORMs con `peewee.py`
- **Avanzados**: Dominar `sqlalchemy.py` y relaciones complejas

### **Para Proyectos Reales**
- **Aplicaciones simples**: Usar Peewee ORM
- **Sistemas complejos**: Implementar con SQLAlchemy
- **Prototipado rápido**: PostgreSQL con psycopg2
- **Interfaces gráficas**: Combinar Tkinter con cualquier ORM

## 📋 Requisitos del Sistema

### **Software Base**
- Python 3.12+
- PostgreSQL 12+ o MySQL 8.0+
- Entorno virtual recomendado

### **Librerías Python**
Ver `requirements.txt` en el directorio raíz del proyecto.

## 🔧 Solución de Problemas

### **Errores Comunes**
1. **Error de conexión**: Verificar credenciales en `.env`
2. **Módulo no encontrado**: Activar entorno virtual
3. **Tabla no existe**: Ejecutar scripts de creación primero
4. **Permisos insuficientes**: Verificar privilegios de BD

### **Compatibilidad**
- ✅ Linux (Ubuntu, CentOS, Debian)
- ✅ macOS (con Homebrew)
- ✅ Windows (con Python oficial)

## 🎓 Recursos de Aprendizaje

- **Documentación oficial** de cada ORM utilizado
- **Ejemplos progresivos** desde básico hasta avanzado
- **Comentarios explicativos** en español en cada archivo
- **Patrones de diseño** aplicados a bases de datos

## 📞 Notas Técnicas

### **Seguridad**
- Las credenciales hardcodeadas son solo para **propósitos educativos**
- En producción, **siempre usar variables de entorno**
- Implementar **validación de entrada** en aplicaciones reales

### **Performance**
- Los ejemplos priorizan **claridad sobre optimización**
- Para producción, considerar **connection pooling**
- Implementar **índices apropiados** en tablas reales

---

*Este proyecto representa un aprendizaje integral de bases de datos con Python, desde conceptos básicos hasta implementaciones avanzadas con ORMs modernos.*