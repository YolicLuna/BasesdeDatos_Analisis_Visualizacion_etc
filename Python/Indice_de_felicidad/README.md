# Análisis del Índice de Felicidad Global

Proyecto de análisis del Índice de Felicidad Global utilizando Python para estudiar qué factores socioeconómicos influyen en el nivel de bienestar de los diferentes países del mundo durante 2015-2019.

---

## Objetivo
Analizar datos de felicidad para identificar:
* Factores que influyen en el bienestar de los países.
* Correlaciones entre variables socioeconómicas y el índice de felicidad.
* Tendencias y evolución temporal del bienestar global. 

---

## Fuente de datos
* Datos del **Informe de Felicidad Mundial** (World Happiness Report).
* Información de felicidad por país para los años 2015, 2016, 2017, 2018 y 2019.
* Archivos CSV separados por año en la carpeta `Data_bases/`.

---

## Tecnologías utilizadas
* Python.
* Pandas.
* Matplotlib.
* Seaborn.
* Jupyter Notebook.

Dependencias definidas en `requirements.txt`

---

## Análisis realizado
* Carga y unificación de datos de 5 años diferentes.
* Limpieza y preparación de datos.
* Análisis exploratorio y estadísticas descriptivas.
* Matriz de correlación entre variables.
* Visualización de distribuciones y relaciones.
* Análisis temporal de tendencias (2015-2019).
* Comparación de países más y menos felices.
* Análisis de causalidades potenciales entre variables.

---

## Visualizaciones
El análisis incluye:
* Histogramas y gráficas de distribución.
* Diagramas de cajas (boxplots) para valores atípicos.
* Matriz de correlación heatmap.
* Gráficos de evolución temporal.
* Scatter plots entre GDP per Capita y Happiness Score.
* Comparativas de top 5 países más y menos felices.

---

## Insights

* **GDP per Capita y Salud**: Son los predictores más fuertes de felicidad (correlaciones > 0.74 y 0.79).
* **Estabilidad Global**: El índice de felicidad mundial se mantiene estable entre 2015-2019.
* **Desigualdades Significativas**: Existen diferencias profundas entre países desarrollados y en desarrollo.
* **Multifactorialidad**: La felicidad depende de múltiples variables que reflejan la calidad de vida integral.
* **Países Destacados**: Finlandia, Dinamarca y Noruega lideran en 2019; Sudán del Sur es el menos feliz.

---

## Conceptos aplicados
* Análisis exploratorio de datos (EDA).
* Correlación y análisis multivariante.
* Series temporales y análisis de tendencias.
* Estadística descriptiva.
* Visualización de datos complejos.
* Análisis comparativo entre grupos.

---

## Cómo ejecutar

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar el notebook:

```bash
jupyter notebook
```

3. Abrir:

```
indice_felicidad.ipynb
```

---

## Enfoque del proyecto
Este proyecto se enfoca en el análisis factorial de datos multivariantes para entender qué factores socioeconómicos contribuyen al bienestar. Es aplicable a:
* Políticas públicas y desarrollo social.
* Investigación en ciencia de datos.
* Análisis de indicadores de calidad de vida.
* Estudios comparativos internacionales.
