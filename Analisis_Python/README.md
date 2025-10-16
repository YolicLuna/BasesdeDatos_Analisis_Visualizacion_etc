# Análisis de Datos con Python

Esta carpeta contiene los apuntes que tome del bootcamp de análisis de datos de la plataforma **Código Facilito**, enfocado en las librerías fundamentales para el análisis de datos en Python: **NumPy** y **Pandas**.

## Descripción

El contenido de esta carpeta documenta el proceso de aprendizaje de las herramientas esenciales para la manipulación, análisis y procesamiento de datos usando Python. Se abordan desde conceptos básicos hasta técnicas avanzadas de filtrado, agrupamiento y análisis estadístico.

## Estructura del Proyecto

```
Analisis_Python/
├── README.md
├── Numpy/
│   ├── numpy.ipynb
│   ├── archivo.txt
│   ├── arreglo_binario.npy
│   └── matriz.csv
└── Pandas/
    ├── pandas.ipynb
    └── Breast_cancer_dataset.csv
```

---

## 📊 Índice de Contenidos

### 🔢 [NumPy - Computación Científica](./Numpy/numpy.ipynb)

**Conceptos Fundamentales:**
- **Introducción a NumPy**: Importación y conceptos básicos
- **Arreglos (Arrays)**: Creación, propiedades y manipulación
- **Propiedades de Arreglos**: `size`, `ndim`, `dtype`, `shape`, `id`

**Operaciones y Manipulación:**
- **Operaciones Matemáticas**: Suma, resta, multiplicación, división elemento a elemento
- **Funciones de Creación**: `np.arange()`, `np.zeros()`, `np.ones()`, `np.random`
- **Tipos de Datos**: Especificación con `dtype` (int, float, complex, bool)

**Estructuras Avanzadas:**
- **Matrices Bidimensionales**: Creación y manipulación de matrices
- **Indexación y Slicing**: Acceso a elementos específicos y subarreglos
- **Copias vs Vistas**: `copy()` vs `view()` y gestión de memoria

**Métodos de Análisis:**
- **Métodos de Agregación**: `sum()`, `min()`, `max()`, `mean()`, `std()`
- **Transposición**: Uso de `.T` para intercambiar filas y columnas
- **Filtros y Condiciones**: Operadores lógicos y filtrado condicional

**Técnicas Avanzadas:**
- **Indexación Avanzada**: Acceso mediante listas de índices
- **Operaciones por Filas/Columnas**: Análisis específico por dimensiones
- **Condiciones Múltiples**: Uso de operadores `&` (AND) y `|` (OR)

---

### 🐼 [Pandas - Análisis de Datos](./Pandas/pandas.ipynb)

**Estructuras de Datos:**
- **Series**: Creación, propiedades (`size`, `dtype`, `shape`, `index`)
- **DataFrames**: Construcción desde diccionarios, manipulación de índices
- **Manejo de Valores Nulos**: `np.nan`, `isnull()`, `notnull()`

**Manipulación de DataFrames:**
- **Acceso a Datos**: Selección de columnas y filas
- **Agregar Columnas**: Incorporación de nuevas Series
- **Propiedades**: `columns`, `values`, `index`

**Indexación y Selección:**
- **Atributo `loc`**: Acceso basado en etiquetas de índice
- **Atributo `iloc`**: Acceso basado en posición numérica
- **Subdataframes**: Creación de vistas parciales de datos

**Filtrado y Condiciones:**
- **Filtros Simples**: Condiciones de igualdad y comparación
- **Filtros Complejos**: Combinación con operadores lógicos `&` y `|`
- **Métodos de String**: `startswith()`, `endswith()`, `contains()`

**Análisis Avanzado:**
- **Ordenamiento**: `sort_values()` con parámetros `ascending`
- **Búsqueda por Rangos**: Método `between()` para filtros de rango
- **Búsqueda entre Opciones**: Método `isin()` para múltiples valores
- **Agrupamiento**: `groupby()` para análisis estadístico por grupos

**Dataset Utilizado:**
- **Breast Cancer Dataset**: Análisis de datos médicos con columnas como `diagnosis`, `radius_mean`, `texture_mean`, `perimeter_mean`, `fractal_dimension_worst`, etc.

---

## 🎯 Objetivos de Aprendizaje

1. **Dominar NumPy** para operaciones numéricas eficientes y manipulación de arrays multidimensionales
2. **Comprender Pandas** para el análisis exploratorio de datos y manipulación de estructuras tabulares
3. **Aplicar técnicas de filtrado** y selección de datos basadas en condiciones complejas
4. **Realizar análisis estadístico** usando métodos de agregación y agrupamiento
5. **Manejar datos reales** mediante datasets como el de cáncer de mama para práctica aplicada

---

## 🔧 Tecnologías Utilizadas

- **Python 3.x**
- **NumPy**: Para computación científica y manejo de arrays
- **Pandas**: Para análisis y manipulación de datos
- **Jupyter Notebooks**: Para desarrollo interactivo y documentación

---

## 📈 Nivel de Contenido

**Principiante a Intermedio**: Los notebooks cubren desde conceptos básicos hasta técnicas avanzadas de análisis de datos, siendo ideales para estudiantes que buscan una base sólida en las herramientas fundamentales del análisis de datos con Python.
