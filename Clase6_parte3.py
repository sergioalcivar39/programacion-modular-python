# ======================================================
# Problema 3: Sistema de Navegación para Vehículo Autónomo
# ======================================================

# Función para leer datos de sensores
def leer_sensores():
    """
    Simula la lectura de sensores de proximidad para esto tenemos que poner un valor y que asi lo recoja.
    """
    distancia = float(input("Ingrese distancia al obstáculo (metros): "))
    return distancia


# Procedimiento para calcular la ruta óptima
def calcular_ruta():
    """
    Simula el cálculo de la mejor ruta.
    """
    print("Calculando ruta óptima hacia el destino...")


# Función para detectar y evitar obstáculos
def detectar_obstaculo(distancia):
    """
    Determina si hay un obstáculo peligroso mediante bucles if.
    """
    if distancia < 5:
        print("Obstáculo detectado. Cambiando ruta.")
        return True
    else:
        print("Ruta despejada.")
        return False


# Procedimiento para ajustar la velocidad
def ajustar_velocidad(obstaculo):
    """
    Ajusta la velocidad del vehículo según las condiciones mediante blucles if
    # no pone el igual igual  == porque el poner solo un booleano como esta escrito este significa que lo compara a true.
    """
    if obstaculo:
        print("Reduciendo velocidad por seguridad.")
    else:
        print("Velocidad normal.")


# ======================================================
# Programa principal
# ======================================================

# Se llaman a las funciones anteriormente creadas 

print("Sistema de Navegación de Vehículo Autónomo")

# Leer sensores
distancia = leer_sensores()

# Calcular ruta
calcular_ruta()

# Detectar obstáculo
hay_obstaculo = detectar_obstaculo(distancia)

# Ajustar velocidad
ajustar_velocidad(hay_obstaculo)