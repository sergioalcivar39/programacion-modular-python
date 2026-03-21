# problema4_sensores.py

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# DATOS DE SENSORES (5 sensores x 5 tiempos)
# Filas = momentos en el tiempo
# Columnas = sensores
# --------------------------------------------------

datos = np.random.randint(20, 100, (5, 5))

print("=== MATRIZ DE DATOS ===")
print(datos)

# --------------------------------------------------
# CÁLCULO DE PROMEDIOS
# --------------------------------------------------

# Promedio por fila (cada momento en el tiempo)
prom_filas = np.mean(datos, axis=1)

# Promedio por columna (cada sensor)
prom_columnas = np.mean(datos, axis=0)

# --------------------------------------------------
# DESVIACIÓN ESTÁNDAR
# --------------------------------------------------

std_filas = np.std(datos, axis=1)
std_columnas = np.std(datos, axis=0)

# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

print("\n=== PROMEDIOS POR FILA (tiempo) ===")
print(prom_filas)

print("\n=== PROMEDIOS POR COLUMNA (sensores) ===")
print(prom_columnas)

print("\n=== DESVIACIÓN ESTÁNDAR POR FILA ===")
print(std_filas)

print("\n=== DESVIACIÓN ESTÁNDAR POR COLUMNA ===")
print(std_columnas)

# --------------------------------------------------
# VISUALIZACIÓN
# --------------------------------------------------

plt.figure()

plt.plot(prom_columnas, marker='o')
plt.title("Promedio de Temperatura por Sensor")
plt.xlabel("Sensor")
plt.ylabel("Temperatura Promedio")

plt.grid()

plt.show()