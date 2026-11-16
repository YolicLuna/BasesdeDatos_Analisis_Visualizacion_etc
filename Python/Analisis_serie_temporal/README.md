# Análisis de Serie Temporal

Proyecto de análisis de series temporales utilizando Python para estudiar el comportamiento de datos a lo largo del tiempo y detectar tendencias, patrones y componentes clave.

---

## Objetivo
Analizar datos temporales para identificar:
* Tendencias.
* Estacionalidad.
* Comportamientos a lo largo del tiempo.

---

## Fuente de datos
* Datos obtenidos mediante la librería `yfinance`.
* Información financiera histórica (ej. precios de activos).

---

## Tecnologías utilizadas
* Python.
* Pandas.
* Matplotlib.
* Statsmodels.
* yfinance.
* Jupyter Notebook.

Dependencias definidas en `requirements.txt` 

---

## Análisis realizado
* Obtención de datos desde API (yfinance).
* Limpieza y preparación de datos.
* Visualización de la serie temporal.
* Análisis de tendencia.
* Descomposición de la serie (trend, seasonality, residual).
* Interpretación de patrones.

---

## Visualizaciones
El análisis incluye:
* Gráficas de evolución temporal
* Identificación de tendencias
* Componentes de la serie (tendencia, estacionalidad, ruido)

---

## Insights

* Se identifican patrones en el comportamiento del activo a lo largo del tiempo.
* La serie presenta tendencias que pueden ser analizadas para entender su evolución.
* La descomposición permite separar señales clave del ruido.

---

## Conceptos aplicados
* Series temporales.
* Análisis de tendencia.
* Estacionalidad.
* Descomposición de series.
* Visualización de datos.
* Uso de datos financieros.

---

## Cómo ejecutar

1. Instalar dependencias:

```bash id="cmd8"
pip install -r requirements.txt
```

2. Ejecutar el notebook:

```bash id="cmd9"
jupyter notebook
```

3. Abrir:

```id="nb2"
serie_temporal.ipynb
```

---

## Enfoque del proyecto
Este proyecto se enfoca en el análisis temporal de datos, una técnica clave en:
* Finanzas.
* Forecasting.
* Ciencia de datos.
