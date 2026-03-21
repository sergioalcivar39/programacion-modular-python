# problema5_transformaciones.py

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# PUNTOS ORIGINALES (figura simple: cuadrado)
# --------------------------------------------------

puntos = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [1, 2]
])

print("Puntos originales:")
print(puntos)

# --------------------------------------------------
# MATRIZ DE ROTACIÓN (45 grados)
# --------------------------------------------------

theta = np.radians(45)

matriz_rotacion = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# --------------------------------------------------
# TRANSFORMACIÓN
# --------------------------------------------------

puntos_transformados = puntos @ matriz_rotacion

print("\nPuntos transformados:")
print(puntos_transformados)

# --------------------------------------------------
# VISUALIZACIÓN
# --------------------------------------------------

plt.figure()

# Original
plt.scatter(puntos[:, 0], puntos[:, 1], label="Original")

# Transformado
plt.scatter(puntos_transformados[:, 0], puntos_transformados[:, 1], label="Rotado")

plt.title("Transformación: Rotación de puntos")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

plt.show()