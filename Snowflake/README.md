# Prácticas de Python y Snowflake

Repositorio de prácticas orientadas a la integración de Python con Snowflake para conectar con bases de datos, automatizar cargas, analizar información y aplicar técnicas de machine learning.
Esta carpeta contiene ejercicios orientados a desarrollar habilidades en:
* Conexión y ejecución de consultas SQL desde Python.
* Carga y automatización de datos en Snowflake.
* Transformación de datos con Snowpark.
* Visualización y creación de dashboards interactivos.
* Análisis predictivo y evaluación de modelos.

---

## Proyectos

### [Conexión de Python con Snowflake](./1.-python_snowflake.ipynb)
Práctica introductoria para conectarse a Snowflake mediante Python y ejecutar consultas SQL.
* Configuración de la conexión con `snowflake.connector`.
* Selección de warehouse y base de datos.
* Ejecución de consultas sobre los datos disponibles.
* Extracción de resultados para trabajar con Pandas.

**Enfoque:** conexión a Snowflake + SQL + Pandas

---

### [Automatización de cargas de datos](./2.-automatizacion.ipynb)
Ejercicio para crear una tabla en Snowflake y cargar información desde el archivo [dataset.csv](./dataset.csv).
* Creación y configuración de objetos de Snowflake.
* Carga del archivo mediante `PUT` y `COPY INTO`.
* Consulta de la tabla `CAMPAING_DATA_PYTHON`.
* Conversión de resultados a DataFrames de Pandas.

**Enfoque:** automatización + carga de datos + SQL

---

### [Análisis con Snowpark](./3.-snowpark.ipynb)
Práctica de transformación y análisis de datos utilizando sesiones de Snowpark para trabajar con tablas de Snowflake.
* Creación de sesiones Snowpark.
* Selección y filtrado de datos.
* Agregaciones por región.
* Análisis de métricas como visualizaciones y clics.

**Enfoque:** Snowpark + transformación de datos + agregaciones

---

### [Análisis predictivo y machine learning](./4.-Analisis_predictivo_y_ML.ipynb)
Análisis de ventas diarias utilizando datos de Snowflake y un modelo de regresión lineal.
* Consulta de datos de ventas.
* Visualización de resultados con Plotly.
* Entrenamiento de un modelo con scikit-learn.
* Evaluación mediante el error cuadrático medio (MSE).
* Guardado y transferencia del modelo con Joblib y un stage de Snowflake.

**Enfoque:** análisis predictivo + regresión lineal + evaluación de modelos

---

### [Dashboard de análisis de datos](./Automatizacion_analisis_datos.py)
Aplicación interactiva desarrollada con Streamlit y Snowpark para consultar y explorar datos de ventas.
* Filtros por región, nación y segmento de mercado.
* Consultas sobre `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1`.
* Gráficos de barras, dispersión y pastel con Plotly.
* Tabla interactiva con los resultados filtrados.

**Ejecución:** `streamlit run Automatizacion_analisis_datos.py`

---

## Enfoque de la carpeta
Los proyectos de esta sección están orientados a:
* Integrar Python con plataformas de datos en la nube.
* Automatizar la carga y consulta de información.
* Utilizar Snowpark para transformar datos cerca de su origen.
* Construir visualizaciones y herramientas interactivas.
* Aplicar modelos de machine learning sobre datos almacenados en Snowflake.

---

## Tecnologías utilizadas
* Python.
* Snowflake Connector for Python.
* Snowflake Snowpark.
* Pandas.
* Jupyter Notebook.
* Streamlit.
* Plotly.
* scikit-learn.
* Joblib.

---

## Datos y modelos
El archivo [dataset.csv](./dataset.csv) contiene datos de campañas con información sobre fechas, regiones, clics, impresiones, visualizaciones y costes.

Los archivos `model.joblib` y `model.joblib.gz` son artefactos locales relacionados con el modelo predictivo. Los archivos de modelo están excluidos del control de versiones mediante `.gitignore` y no son necesarios para ejecutar todas las prácticas.

---

## Requisitos y ejecución
Instalar las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

Después, abrir los notebooks en Jupyter y ejecutarlos en el orden recomendado:
1. Conexión de Python con Snowflake.
2. Automatización de cargas de datos.
3. Análisis con Snowpark.
4. Análisis predictivo y machine learning.

Para iniciar el dashboard:

```bash
streamlit run Automatizacion_analisis_datos.py
```

## Configuración de la conexión
Las prácticas leen las credenciales desde un archivo local llamado `config`, ubicado en la carpeta `.snowsql` del perfil de usuario de Windows. El archivo no tiene extensión y se utiliza para evitar escribir las credenciales directamente en los notebooks o en el script.

Crear la carpeta y abrir el archivo con PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.snowsql"
notepad "$env:USERPROFILE\.snowsql\config"
```

Dentro del archivo, añadir una conexión con esta estructura y sustituir los valores entre `< >` por los datos de la cuenta de Snowflake:

```ini
[connections.example]
accountname = <nombre_de_la_cuenta>
username = <usuario_de_snowflake>
password = <contraseña_de_snowflake>
```

El nombre de la sección debe coincidir con `connections.example`, ya que los ejercicios buscan exactamente esa sección. Después, el código utiliza `configparser` para leer `accountname`, `username` y `password`. El conector crea la conexión con `snowflake.connector.connect()` y Snowpark utiliza esos mismos valores para crear una sesión mediante `Session.builder.configs()`.

Una vez creado el archivo, comprobar que la configuración funciona ejecutando primero el notebook [1.-python_snowflake.ipynb](./1.-python_snowflake.ipynb). No es necesario copiar el archivo dentro del repositorio.

Las prácticas requieren una cuenta de Snowflake y los permisos, warehouses, bases de datos, tablas y stages utilizados por cada ejercicio. Las credenciales deben configurarse localmente y nunca incluirse en el repositorio.

---

## Nota
Cada práctica muestra un flujo diferente de trabajo con Snowflake y puede depender de objetos creados previamente o de datos de ejemplo disponibles en la cuenta.

No se deben publicar credenciales, archivos `.env`, configuraciones de `.snowsql` ni valores sensibles de conexión. La ejecución completa no es independiente del entorno de Snowflake.

---

## Objetivo
Desarrollar habilidades prácticas en ingeniería y análisis de datos utilizando Python, Snowflake y Snowpark, creando una base para trabajar en roles como Data Analyst, Data Engineer o Machine Learning Engineer.
