# 🛠️ Requisitos del Proyecto

Este documento lista todos los programas, librerías y dependencias necesarias para trabajar con este proyecto de análisis de datos y bases de datos.

## 📋 Requisitos del Sistema

### **Sistema Operativo**
- **Linux** (recomendado) / **macOS** / **Windows**
- **Python 3.12+** (recomendado: 3.12.3)

### **Software Base Requerido**

#### **1. Python**
```bash
# Verificar instalación
python --version  # Debe ser 3.12+
```

#### **2. MySQL Server**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server

# macOS (con Homebrew)
brew install mysql

# Windows: Descargar desde mysql.com
```

#### **3. Git** (para clonar el repositorio)
```bash
# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# Windows: Descargar desde git-scm.com
```

---

## 📦 Dependencias de Python

### **Instalación Automática**
```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]
cd BasesdeDatos_Analisis_Visualizacion_etc

# Instalar dependencias
pip install -r requirements.txt
```

### **Librerías Principales**

| Librería | Versión | Propósito |
|----------|---------|-----------|
| **numpy** | 1.26.4 | Computación científica y arrays |
| **pandas** | 2.3.2 | Manipulación y análisis de datos |
| **jupyter** | 1.1.1 | Notebooks interactivos |
| **jupyterlab** | 4.4.7 | Entorno de desarrollo |
| **mysql-connector-python** | 9.4.0 | Conexión con MySQL |
| **matplotlib** | 3.10.6 | Visualización básica |
| **seaborn** | 0.13.2 | Visualización estadística |
| **openpyxl** | 3.1.5 | Manejo de archivos Excel |
| **scikit-learn** | 1.7.1 | Machine learning |
| **scipy** | 1.16.1 | Cálculos científicos |

### **Instalación Manual por Librería**
```bash
pip install numpy==1.26.4
pip install pandas==2.3.2
pip install jupyter==1.1.1
pip install jupyterlab==4.4.7
pip install mysql-connector-python==9.4.0
pip install matplotlib==3.10.6
pip install seaborn==0.13.2
pip install openpyxl==3.1.5
pip install scikit-learn==1.7.1
pip install scipy==1.16.1
```

---

## 🐍 Configuración del Entorno Python

### **Opción 1: Entorno Virtual (Recomendado)**
```bash
# Crear entorno virtual
python -m venv datos-analisis
cd datos-analisis

# Activar entorno
# Linux/macOS:
source bin/activate
# Windows:
Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### **Opción 2: Conda Environment**
```bash
# Crear entorno con conda
conda create -n datos-analisis python=3.12
conda activate datos-analisis

# Instalar dependencias principales
conda install numpy pandas jupyter
pip install -r requirements.txt
```

---

## 🗄️ Configuración de MySQL

### **1. Instalación y Configuración Inicial**
```sql
-- Crear usuario para el proyecto
CREATE USER 'analisis_user'@'localhost' IDENTIFIED BY 'password123';

-- Otorgar permisos
GRANT ALL PRIVILEGES ON *.* TO 'analisis_user'@'localhost';
FLUSH PRIVILEGES;
```

### **2. Configuración de Base de Datos**
```sql
-- Crear base de datos principal
CREATE DATABASE Alumnos_titulados;
USE Alumnos_titulados;

-- Las tablas se crearán automáticamente al ejecutar los scripts SQL
```

### **3. Archivos de Datos**
Los siguientes archivos se encuentran en el proyecto:
- `Ejercicios/Analisis_con_MySQL.sql` - Script completo con datos de ejemplo
- `Analisis_Python/Numpy/archivo.txt` - Datos para ejercicios NumPy
- `Analisis_Python/Numpy/matriz.csv` - Dataset CSV para prácticas
- `Analisis_Python/Pandas/Breast_cancer_dataset.csv` - Dataset para análisis

---

## 🚀 Instalación Paso a Paso

### **1. Clonar el Repositorio**
```bash
git clone [URL_DEL_REPOSITORIO]
cd BasesdeDatos_Analisis_Visualizacion_etc
```

### **2. Configurar Python**
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### **3. Configurar MySQL**
```bash
# Iniciar MySQL
sudo systemctl start mysql  # Linux
brew services start mysql   # macOS

# Conectar y crear base de datos
mysql -u root -p
```

### **4. Iniciar Jupyter**
```bash
# Opción 1: Jupyter Notebook
jupyter notebook

# Opción 2: JupyterLab (recomendado)
jupyter lab
```

### **5. Verificar Instalación**
```python
# Ejecutar en Jupyter/Python
import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

print("✅ Todas las librerías funcionan correctamente")
```

---

## 🔧 Herramientas Adicionales (Opcionales)

### **Editores de Código Recomendados**
- **VS Code** con extensiones:
  - Python
  - Jupyter
  - MySQL
  - GitLens

### **Herramientas de Base de Datos**
- **MySQL Workbench** (GUI para MySQL)
- **phpMyAdmin** (interfaz web)
- **DBeaver** (cliente universal)

### **Control de Versiones**
- **Git** (requerido)
- **GitHub Desktop** (opcional, GUI)

---

## ⚠️ Notas Importantes

### **Compatibilidad**
- **NumPy 1.26.4** es requerido (versiones 2.x pueden causar conflictos)
- **Python 3.12+** es recomendado para compatibilidad completa
- **MySQL 8.0+** para características avanzadas

### **Solución de Problemas Comunes**

#### **Error de NumPy**
```bash
# Si hay conflictos con NumPy 2.x
pip uninstall numpy
pip install numpy==1.26.4
```

#### **Error de Conexión MySQL**
```bash
# Verificar que MySQL esté ejecutándose
sudo systemctl status mysql    # Linux
brew services list | grep mysql # macOS
```

#### **Error de Jupyter Kernel**
```bash
# Reinstalar kernel
python -m ipykernel install --user --name=datos-analisis
```

---

## 📞 Soporte

Si encuentras problemas con la instalación:

1. **Verifica versiones**: Asegúrate de usar las versiones especificadas
2. **Consulta logs**: Revisa mensajes de error completos
3. **Documenta**: Los archivos README en cada carpeta tienen información específica
4. **Entorno limpio**: Considera usar un entorno virtual nuevo

---

*Este archivo se actualiza conforme se agregan nuevas dependencias al proyecto.*