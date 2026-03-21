# problema3_imagen3d.py

import numpy as np

# --------------------------------------------------
# CREACIÓN DEL VOLUMEN 3D (simulación de imágenes médicas)
# Cada "capa" es una imagen 2D
# --------------------------------------------------

volumen = np.random.randint(0, 256, (5, 5, 5))  # valores tipo imagen (0-255)

print("=== CAPA ORIGINAL (slice 2) ===")
print(volumen[:, :, 2])

# --------------------------------------------------
# FUNCIÓN DE SUAVIZADO (FILTRO PROMEDIO 3D)
# --------------------------------------------------

def suavizar(vol):
    nuevo = vol.copy()
    
    # Recorremos evitando bordes
    for i in range(1, vol.shape[0] - 1):
        for j in range(1, vol.shape[1] - 1):
            for k in range(1, vol.shape[2] - 1):
                
                # Vecindario 3x3x3 (27 valores)
                bloque = vol[i-1:i+2, j-1:j+2, k-1:k+2]
                
                # Promedio
                nuevo[i, j, k] = int(np.mean(bloque))
    
    return nuevo

# --------------------------------------------------
# APLICAR SUAVIZADO
# --------------------------------------------------

volumen_suavizado = suavizar(volumen)

print("\n=== CAPA SUAVIZADA (slice 2) ===")
print(volumen_suavizado[:, :, 2])

# --------------------------------------------------
# COMPARACIÓN SIMPLE
# --------------------------------------------------

diferencia = np.abs(volumen - volumen_suavizado)

print("\n=== DIFERENCIA (slice 2) ===")
print(diferencia[:, :, 2])