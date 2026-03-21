# problema2_fluido3d.py

import numpy as np

# --------------------------------------------------
# CREACIÓN DEL FLUIDO (3x3x3)
# Cada celda representa presión en un punto del espacio
# --------------------------------------------------

fluido = np.random.rand(3, 3, 3) * 100  # valores de presión inicial

print("=== ESTADO INICIAL DEL FLUIDO ===")
print(fluido)

# --------------------------------------------------
# FUNCIÓN DE ACTUALIZACIÓN
# Promedio de vecinos (simulación de propagación)
# --------------------------------------------------

def actualizar_presion(f):
    nuevo = f.copy()
    
    # Solo actualizamos el centro para evitar bordes
    for i in range(1, 2):
        for j in range(1, 2):
            for k in range(1, 2):
                
                vecinos = [
                    f[i+1, j, k], f[i-1, j, k],
                    f[i, j+1, k], f[i, j-1, k],
                    f[i, j, k+1], f[i, j, k-1]
                ]
                
                nuevo[i, j, k] = sum(vecinos) / len(vecinos)
    
    return nuevo

# --------------------------------------------------
# SIMULACIÓN (varios pasos en el tiempo)
# --------------------------------------------------

pasos = 5

for t in range(pasos):
    fluido = actualizar_presion(fluido)
    print(f"\n--- Iteración {t+1} ---")
    print(fluido)

# --------------------------------------------------
# INTERPRETACIÓN
# La presión tiende a equilibrarse entre celdas vecinas
# --------------------------------------------------