# Automatización del Análisis de Ventas Regional con Snowflake y Streamlit.

"""
- Problema: Análisis de ventas rwegionales crucial para obtimizar cadena de suministros y estrategias.
Informes mensuales = lentos, limitados, poco interactios, análisis superficial.

- Limitaciones Actuales: Informes estáticos no responden a preguntas profundas: distribución por segmento en regiones, correlaciones, contribución regional, patrones compplejos.

- Solucion: Web App Interactiva: Steamlit + Snowflake + Plotliy = Dashboard automatizado, interactivo y con visualizaciones avanzadas.

- Beneficios Clave: Automatización. interactividad, visualizaciones Plotly para insights profundos, datos en tiempo real, escalabilidad y desarrollo ágil.
"""
import os
import configparser
from snowflake.snowpark import Session
import streamlit as st
import plotly.express as px

DATA_BASE = 'SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.'

st.title('Reporte de Análisis de Ventas Regionales.')
st.write("""
Esta aplicación web permite analizar de forma interactiva 
las ventas regionales  utilizando la base de datos TCP-H de
Snowflake.
"""
)

# Configuración de la conexión a Snowflake.
config_path = os.path.join(os.environ['USERPROFILE'], '.snowsql', 'config')
config = configparser.ConfigParser()
config.read(config_path)

# Se obtienen los parámetros de conexión desde el archivo de configuración.
try:
    account = config['connections.example']['accountname']
    user = config['connections.example']['username']
    password = config['connections.example']['password']
except KeyError as e:
    print(f'Error: {e}')

# Se definen los parámetros de conexión a Snowflake.
connection_parameters = {
    "account": account,
    "user": user,
    "password": password,
    "warehouse": "COMPUTE_WH",
    "database": "DEVMOON_SAMPLE",
    "schema": "PUBLIC",
}

# Se crea la sesión de Snowpark utilizando los parámetros de conexión.
try:
    session = Session.builder.configs(connection_parameters).create()
    print('Conexión exitosa con Snowpark.')
except Exception as e:
    print(f'Error: {e}')

# Función para ejecutar consultas en Snowflake y convertir a Pandas DataFrame
def load_data(query):
    try:
        result_df = session.sql(query).to_pandas()
        return result_df
    except Exception as e:
        st.error(f"Error al ejecutar la consulta: {e}")
        return None

# ---  Widgets de Selección para el Usuario ---
st.sidebar.header("Filtros")

# Selección de Región (con opción de seleccionar todas)
regiones_query = f"SELECT DISTINCT R_NAME FROM {DATA_BASE}REGION ORDER BY R_NAME"
regiones_df = load_data(regiones_query)
if regiones_df is not None:
    regiones_list = ["TODAS"] + regiones_df['R_NAME'].tolist() # Añadir "TODAS" como opción
    region_seleccionada = st.sidebar.selectbox("Selecciona Región", regiones_list, index=0) # "TODAS" por defecto
else:
    region_seleccionada = "TODAS"

# Selección de Nación (dependiente de la región seleccionada)
naciones_list = ["TODAS"] # Inicializar con "TODAS"
nacion_seleccionada = "TODAS" # Valor por defecto
if region_seleccionada and region_seleccionada != "TODAS":
    naciones_query = f"""
        SELECT DISTINCT N.N_NAME
        FROM {DATA_BASE}NATION N
        JOIN {DATA_BASE}REGION R ON N.N_REGIONKEY = R.R_REGIONKEY
        WHERE R.R_NAME = '{region_seleccionada}'
        ORDER BY N.N_NAME
    """
    naciones_df = load_data(naciones_query)
    if naciones_df is not None:
        naciones_list = ["TODAS"] + naciones_df['N_NAME'].tolist()
        nacion_seleccionada = st.sidebar.selectbox("Selecciona Nación", naciones_list, index=0) # "TODAS" por defecto

# Selección de Segmento de Mercado del Cliente (con opción de seleccionar todos)
segmentos_query = f"SELECT DISTINCT C_MKTSEGMENT FROM {DATA_BASE}CUSTOMER ORDER BY C_MKTSEGMENT"
segmentos_df = load_data(segmentos_query)
if segmentos_df is not None:
    segmentos_list = ["TODOS"] + segmentos_df['C_MKTSEGMENT'].tolist() # Añadir "TODOS" como opción
    segmento_seleccionado = st.sidebar.selectbox("Segmento de Mercado", segmentos_list, index=0) # "TODOS" por defecto
else:
    segmento_seleccionado = "TODOS"


# ---  Consulta Principal de Ventas ---
query_ventas = f"""
    SELECT
        R.R_NAME AS REGION,
        N.N_NAME AS NACION,
        C.C_MKTSEGMENT AS SEGMENTO_MERCADO,
        SUM(L.L_EXTENDEDPRICE * (1 - L.L_DISCOUNT)) AS VENTAS_TOTALES
    FROM {DATA_BASE}LINEITEM L
    JOIN {DATA_BASE}ORDERS O ON L.L_ORDERKEY = O.O_ORDERKEY
    JOIN {DATA_BASE}CUSTOMER C ON O.O_CUSTKEY = C.C_CUSTKEY
    JOIN {DATA_BASE}NATION N ON C.C_NATIONKEY = N.N_NATIONKEY
    JOIN {DATA_BASE}REGION R ON N.N_REGIONKEY = R.R_REGIONKEY
    WHERE 1=1 -- Filtro base para añadir condiciones dinámicamente
"""

# ---  Añadir Filtros Dinámicos a la Consulta ---
if region_seleccionada != "TODAS":
    query_ventas += f" AND R.R_NAME = '{region_seleccionada}'"
if nacion_seleccionada != "TODAS" and nacion_seleccionada != None: #Asegurarse de que nacion_seleccionada no sea None
    query_ventas += f" AND N.N_NAME = '{nacion_seleccionada}'"
if segmento_seleccionado != "TODOS":
    query_ventas += f" AND C.C_MKTSEGMENT = '{segmento_seleccionado}'"

query_ventas += """
    GROUP BY R.R_NAME, N.N_NAME, C.C_MKTSEGMENT
    ORDER BY VENTAS_TOTALES DESC
""" # 

# ---  Cargar y Mostrar Datos de Ventas ---
ventas_df = load_data(query_ventas)

if ventas_df is not None and not ventas_df.empty:
    st.subheader("Ventas Totales por Región, Nación y Segmento de Mercado")

    # ---  Visualización con Gráfico de Barras (Plotly) ---
    st.write("Gráfico de Barras Interactivo (Plotly)") # Subtítulo para el gráfico
    fig_bar = px.bar(
        ventas_df,
        x="REGION" if region_seleccionada == "TODAS" else "NACION",
        y="VENTAS_TOTALES",
        color="SEGMENTO_MERCADO", # Añadimos color por segmento para más detalle
        title="Ventas por Región/Nación y Segmento de Mercado",
        labels={'VENTAS_TOTALES': 'Ventas Totales', 'REGION': 'Región', 'NACION': 'Nación', 'SEGMENTO_MERCADO': 'Segmento'} # Etiquetas más descriptivas
    )
    st.plotly_chart(fig_bar, use_container_width=True)


    # ---  Visualización con Gráfico de Dispersión (Plotly) ---
    st.write("Gráfico de Dispersión (Plotly) - Segmento de Mercado vs Ventas") # Subtítulo para el gráfico
    fig_scatter = px.scatter(
        ventas_df,
        x="SEGMENTO_MERCADO",
        y="VENTAS_TOTALES",
        color="REGION" if region_seleccionada == "TODAS" else "NACION", # Color por región o nación
        size='VENTAS_TOTALES', # Tamaño de los puntos por ventas
        hover_data=['REGION', 'NACION'], # Información al pasar el ratón
        title="Distribución de Ventas por Segmento de Mercado",
        labels={'VENTAS_TOTALES': 'Ventas Totales', 'SEGMENTO_MERCADO': 'Segmento', 'REGION': 'Región', 'NACION': 'Nación'} # Etiquetas más descriptivas
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


    # --- Visualización con Gráfico de Pastel (Plotly) ---
    st.write("Gráfico de Pastel (Plotly) - Contribución Regional a las Ventas Totales") # Subtítulo para el gráfico
    region_sales_df = ventas_df.groupby('REGION')['VENTAS_TOTALES'].sum().reset_index() # Agrupar ventas por región
    fig_pie = px.pie(
        region_sales_df,
        names='REGION',
        values='VENTAS_TOTALES',
        title="Contribución de Ventas por Región",
        labels={'REGION': 'Región', 'VENTAS_TOTALES': 'Ventas Totales'} # Etiquetas más descriptivas
    )
    st.plotly_chart(fig_pie, use_container_width=True)


    # ---  Mostrar Datos en Tabla Interactiva (Limitado a 50 filas para mejor visualización) ---
    st.subheader("Datos Detallados de Ventas (Primeros 50 Registros)")
    st.dataframe(ventas_df.head(50), use_container_width=True) # Mostrar solo las primeras 50 filas
else:
    st.info("No hay datos que mostrar con los filtros seleccionados.")

st.caption("Datos obtenidos de la base de datos TPC-H en Snowflake.")
