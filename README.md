# # 📊 Ingeniería con Arreglos Multidimensionales

## 📌 Descripción

Este proyecto presenta la resolución de problemas reales de ingeniería utilizando **arreglos multidimensionales** en Python. Se abordan aplicaciones en análisis estructural, simulación de fluidos, procesamiento de imágenes, análisis de datos y transformaciones geométricas.

El objetivo es demostrar cómo el uso de estructuras de datos como matrices y volúmenes permite modelar y resolver problemas complejos de manera eficiente.

---

## 🧠 Problemas Desarrollados

### 🔹 Problema 1: Análisis de Fuerzas en una Estructura

Se modeló una estructura mediante una matriz 3x3 donde cada elemento representa una fuerza aplicada en un nodo.

* Se calcularon las sumas por filas y columnas
* Se evaluó el equilibrio estructural usando la condición ∑F = 0

📌 Resultado: La estructura no se encuentra en equilibrio.

---

### 🔹 Problema 2: Simulación de Fluido en 3D

Se utilizó un arreglo tridimensional (3x3x3) para representar la presión de un fluido.

* Se implementó una actualización basada en el promedio de vecinos
* Se simuló la propagación de presión en el tiempo

📌 Mejora aplicada: Se actualizaron todas las celdas internas para lograr una simulación más realista.

---

### 🔹 Problema 3: Análisis de Imágenes Médicas en 3D

Se representó un volumen tridimensional como una imagen médica.

* Se aplicó un filtro de promedio (3x3x3)
* Se redujo el ruido en los datos

📌 Resultado: Se logró suavizar la imagen manteniendo su estructura.

---

### 🔹 Problema 4: Manejo de Datos de Sensores

Se analizaron datos de temperatura en una matriz 5x5.

* Se calcularon promedios por filas (tiempo) y columnas (sensores)
* Se calcularon desviaciones estándar
* Se generó una visualización de los datos

📌 Resultado: Se identificaron patrones de comportamiento y variabilidad en los sensores.

---

### 🔹 Problema 5: Transformación de Coordenadas

Se aplicó una transformación lineal a un conjunto de puntos en 2D.

* Se utilizó una matriz de rotación
* Se transformaron los puntos mediante multiplicación matricial
* Se visualizaron los resultados

📌 Resultado: Los puntos fueron rotados correctamente en el plano cartesiano.

---

## ⚙️ Tecnologías Utilizadas

* Python 3.12
* NumPy
* Matplotlib

---

## 🚀 Ejecución del Proyecto

1. Instalar dependencias:

```bash
pip install numpy matplotlib
```

2. Ejecutar los archivos:

```bash
python problema1_fuerzas.py
python problema2_fluido3d.py
python problema3_imagen3d.py
python problema4_sensores.py
python problema5_transformaciones.py
```

---

## ⚡ Eficiencia de la Solución

El uso de arreglos multidimensionales permite:

* Reducir el uso de estructuras complejas
* Optimizar operaciones mediante cálculos vectorizados
* Mejorar el rendimiento en procesamiento de datos
* Facilitar la simulación de sistemas físicos

Esto es fundamental en áreas como ingeniería, inteligencia artificial y simulación científica.

---

## 📌 Conclusión

Los arreglos multidimensionales son herramientas clave para modelar sistemas reales. Su implementación en este proyecto permitió resolver problemas de distintas áreas de la ingeniería de forma eficiente, clara y escalable.

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica académica de programación aplicada a la ingeniería.
