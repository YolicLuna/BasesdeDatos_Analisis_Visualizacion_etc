# Bases de Datos, Análisis y Visualización

![Python](https://img.shields.io/badge/Python-An%C3%A1lisis%20de%20datos-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-Pr%C3%A1cticas-4479A1.svg)
![Snowflake](https://img.shields.io/badge/Snowflake-Datos%20en%20la%20nube-29B5E8.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)

Repositorio de prácticas de datos con diferentes tecnologías. Reúne ejercicios de SQL, Python y Snowflake, análisis exploratorio, visualización, automatización de cargas y trabajo con datos. Cada carpeta organiza un conjunto de prácticas con su propia documentación.

---

## Descripción General

El repositorio está organizado por tecnología y tipo de práctica. La carpeta `MySql` contiene scripts SQL para aprender modelado relacional, consultas y análisis de negocio; `Python` agrupa proyectos de análisis y visualización con distintos datasets; y `SnowflakePracticas` reúne ejercicios para conectar Python con Snowflake, cargar y transformar datos y aplicar análisis predictivo.

Las guías de cada sección describen sus archivos, requisitos y formas de ejecución:

- [Prácticas de MySQL](./MySql/README.md)
- [Proyectos de análisis con Python](./Python/README.md)
- [Prácticas de Python y Snowflake](./SnowflakePracticas/README.md)

### Tecnologías Utilizadas

Las prácticas utilizan MySQL para consultas y modelado de bases de datos; Python con Pandas, NumPy y Jupyter para análisis; y Snowflake junto con su conector y Snowpark para trabajar con datos en la nube. También se incluyen herramientas de visualización como Matplotlib, Seaborn y Plotly, así como Streamlit para crear un dashboard interactivo.

### Arquitectura y Organización del Repositorio

El repositorio no es una aplicación única: cada carpeta contiene ejercicios y proyectos independientes. Los scripts SQL se ejecutan en MySQL; los proyectos de Python se trabajan desde sus notebooks o archivos correspondientes; y las prácticas de Snowflake requieren configurar una cuenta y los objetos de datos utilizados por cada ejercicio.

#### Estructura del Proyecto

```text
BasesdeDatos_Analisis_Visualizacion_etc/
├── README.md
├── Ejemplo.md
├── INSTALLATION.md
├── MySql/
│   ├── README.md
│   ├── Analisis_con_MySQL.sql
│   ├── caso_practico.sql
│   ├── sql_Riaz.sql
│   └── Pixar/
│       ├── Pixar.sql
│       └── pixar_films.csv
├── Python/
│   ├── README.md
│   ├── Analisis_CO2/
│   ├── Analisis_serie_temporal/
│   ├── Indice_de_felicidad/
│   └── Superstore_analisis/
└── SnowflakePracticas/
    ├── README.md
    ├── 1.-python_snowflake.ipynb
    ├── 2.-automatizacion.ipynb
    ├── 3.-snowpark.ipynb
    ├── 4.-Analisis_predictivo_y_ML.ipynb
    ├── Automatizacion_analisis_datos.py
    ├── dataset.csv
    └── requirements.txt
```

### Secciones del Repositorio

#### MySQL — Consultas y modelado de bases de datos

La carpeta [MySql](./MySql/) contiene ejercicios para practicar SQL y el diseño de bases de datos relacionales. Incluye la creación de tablas relacionadas con datos de estudiantes, un caso de análisis de ventas para una tienda, consultas y carga de datos de películas de Pixar desde CSV, y un modelo de inventario, ventas y pedidos.

Entre los temas trabajados se encuentran las llaves foráneas, la integridad referencial, los `JOIN`, las agregaciones, el filtrado, la importación de datos y el análisis de negocio. Consulta [su README](./MySql/README.md) para ver el detalle de cada script y las recomendaciones de estudio.

#### Python — Análisis exploratorio y visualización

La carpeta [Python](./Python/) reúne proyectos de análisis con datasets reales. Sus subcarpetas cubren el análisis de emisiones de CO₂ per cápita, series temporales financieras, el Índice de Felicidad Mundial y datos de ventas de Superstore.

Las prácticas exploran relaciones entre variables, correlaciones, tendencias temporales, comparaciones entre países y métricas de negocio. Se apoyan principalmente en Python, Pandas, NumPy, Matplotlib, Seaborn, Statsmodels y Jupyter Notebook. Cada proyecto incluye documentación propia; el [README de Python](./Python/README.md) sirve como índice de la sección.

#### SnowflakePracticas — Python, Snowflake y Snowpark

La carpeta [SnowflakePracticas](./SnowflakePracticas/) desarrolla flujos de trabajo con datos almacenados en Snowflake: conexión y consultas desde Python, automatización de cargas desde CSV, transformaciones con Snowpark, análisis predictivo de ventas y un dashboard interactivo.

Los ejercicios utilizan Snowflake Connector for Python, Snowpark, Pandas, Jupyter, Streamlit, Plotly y scikit-learn. El archivo `requirements.txt` contiene las dependencias de esta sección. Para configurar la conexión, revisar los requisitos de cuenta y ejecutar las prácticas, consulta el [README de SnowflakePracticas](./SnowflakePracticas/README.md).

---

## Requisitos y Ejecución

Los requisitos dependen de la práctica: para los ejercicios SQL se necesita MySQL y un cliente compatible; los proyectos de análisis requieren Python y las bibliotecas indicadas en su documentación; las prácticas en la nube requieren además una cuenta de Snowflake y los permisos y objetos que utiliza cada ejercicio.

No hay un único comando de instalación o ejecución para todo el repositorio. Antes de empezar, abre el README de la carpeta correspondiente y sigue sus instrucciones específicas.

## Datos y Credenciales

Algunas prácticas incluyen archivos CSV como datos de entrada. Las prácticas de Snowflake requieren configurar localmente las credenciales de conexión y los recursos de la cuenta descritos en su documentación. No guardes contraseñas, archivos de configuración sensibles ni otros secretos en el repositorio.

---

## Objetivo

Desarrollar habilidades prácticas en bases de datos, análisis y visualización de datos mediante ejercicios con diferentes herramientas y tecnologías, desde consultas SQL y modelado relacional hasta análisis con Python y procesamiento de datos en Snowflake.
