# Análisis Superstore

Proyecto de análisis de datos de ventas utilizando Python para examinar el rendimiento de una tienda, identificar patrones de venta y evaluar la rentabilidad por diferentes dimensiones de negocio.

---

## Objetivo
Analizar datos de ventas de Superstore para:
* Entender el rendimiento de ventas por región y categoría.
* Identificar las subcategorías más rentables.
* Evaluar el impacto de descuentos en la ganancia.
* Analizar patrones de venta por segmento de cliente.

---

## Fuente de datos
* Dataset: `Superstore.csv`
* Contiene información de órdenes, clientes y productos.
* Incluye datos de ventas, ganancias y descuentos.
* Cobertura geográfica: múltiples regiones, ciudades y estados.

---

## Tecnologías utilizadas
* Python.
* Pandas.
* Matplotlib.
* Jupyter Notebook.

Dependencias definidas en `requirements.txt`

---

## Análisis realizado
* Carga y exploración completa del dataset (9,994 registros, 21 columnas).
* Análisis de información: verificación de datos completos sin valores faltantes.
* Estadísticas descriptivas: identificación de variabilidad y valores extremos.
* Análisis regional: ventas y ganancias agregadas por región y categoría.
* Análisis de subcategorías: ranking de rentabilidad por región identificando subcategorías de alto y bajo desempeño.
* Estudio del impacto de descuentos: análisis de descuentos promedio y su relación con ganancias por segmento.
* Análisis de segmentación: ventas cruzadas por segmento de cliente y región.
* Análisis de volumen: crosstab de cantidad de pedidos por categoría y región.

---

## Visualizaciones
El análisis incluye:
* Gráficos de barras de ventas por región y categoría (Technology destaca en en todas las regiones).
* Gráficos del descuento promedio por segmento de cliente.
* Tablas de resumen agregadas de ventas y ganancias.
* Análisis cruzado (crosstab) de volumen de pedidos por categoría y región.
* Tabla de ventas por segmento de cliente en cada región.

---

## Insights

* **Technology lidera en ventas:** La categoría Technology genera las mayores ventas en todas las regiones, con un pico notable en la región East.
* **Rentabilidad por región:** West y East presentan los valores más altos de ventas y ganancias, mientras que South registra el desempeño más bajo.
* **Furniture con pérdidas:** La categoría Furniture presenta pérdidas en la región Central, indicando un área de mejora crítica.
* **Subcategorías destacadas:** Copiers y Phones generan altas ganancias en ciertas regiones, mientras que Machines y Bookcases muestran bajo desempeño.
* **Segmento más rentable:** Home Office presenta la mayor ganancia promedio a pesar de ofrecer descuentos más bajos.
* **Impacto de descuentos:** Los descuentos pueden alcanzar hasta el 80%, con variabilidad en su impacto según el segmento.
* **Volumen de pedidos:** Office Supplies concentra la mayor cantidad de pedidos en todas las regiones, seguida por Furniture y Technology.
* **Segmentación de clientes:** El segmento Consumer lidera en volumen de ventas en todas las regiones, seguido por Corporate y Home Office.

---

## Conceptos aplicados
* Agregación de datos (groupby, sum).
* Análisis multidimensional (región, categoría, subcategoría, segmento).
* Tablas dinámicas (pivot tables).
* Análisis de crosstabs.
* Correlación entre descuentos y rentabilidad.
* Visualización de datos comparativos.

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
superstore.ipynb
```

---

## Enfoque del proyecto
Este proyecto se enfoca en el análisis exploratorio de datos de negocio (EDA), una técnica clave en:
* Análisis de ventas.
* Inteligencia empresarial.
* Toma de decisiones basada en datos.
* Identificación de oportunidades de mejora.
