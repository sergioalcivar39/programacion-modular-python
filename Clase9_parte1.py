import numpy as np

# --------------------------------------------------
# MATRIZ DE FUERZAS (3x3)
# Cada elemento representa una fuerza en un nodo (en Newtons)
# Valores positivos: fuerza en una dirección
# Valores negativos: fuerza en dirección opuesta
# --------------------------------------------------

fuerzas = np.array([
    [10, -5,  3],
    [ 4,  0, -2],
    [ 7, -3,  6]
])

# --------------------------------------------------
# CÁLCULO DE REACCIONES
# Según la estática: suma de fuerzas = 0 en equilibrio
# --------------------------------------------------

# Suma de fuerzas por filas (equilibrio horizontal por nodo)
reacciones_filas = np.sum(fuerzas, axis=1)

# Suma de fuerzas por columnas (equilibrio vertical por nodo)
reacciones_columnas = np.sum(fuerzas, axis=0)

# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

print("=== MATRIZ DE FUERZAS ===")
print(fuerzas)

print("\n=== REACCIONES POR FILA ===")
for i, val in enumerate(reacciones_filas):
    print(f"Fila {i}: {val} N")

print("\n=== REACCIONES POR COLUMNA ===")
for j, val in enumerate(reacciones_columnas):
    print(f"Columna {j}: {val} N")

# --------------------------------------------------
# INTERPRETACIÓN
# Si la suma es diferente de 0, hay una fuerza neta
# (el nodo no está en equilibrio)
# --------------------------------------------------

if np.allclose(reacciones_filas, 0) and np.allclose(reacciones_columnas, 0):
    print("\nLa estructura está en equilibrio.")
else:
    print("\nLa estructura NO está en equilibrio.")