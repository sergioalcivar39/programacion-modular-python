# ======================================================
# Problema 1: Control de Temperatura en un Edificio Inteligente
# ======================================================

# Función para leer datos de sensores de temperatura
def leer_temperatura():
    """
    Esta función solicita al usuario la temperatura actual
    medida por los sensores del edificio.
    """
    temperatura = float(input("Ingrese la temperatura actual: "))
    return temperatura


# Función para calcular la temperatura óptima
def calcular_temperatura_optima(temp_actual):
    """
    Calcula la temperatura ideal dependiendo de la temperatura actual.
    """
    if temp_actual < 20:
        return 22
    elif temp_actual > 28:
        return 24
    else:
        return temp_actual


# Procedimiento para enviar señales al sistema de climatización
def ajustar_climatizacion(temp_objetivo):
    """
    Ajusta el sistema de calefacción o refrigeración
    según la temperatura objetivo.
    """
    print("Ajustando el sistema a", temp_objetivo, "grados")


# Función para registrar el consumo de energía
def registrar_consumo():
    """
    Simula el registro del consumo energético del sistema.
    """
    consumo = 5  # valor simulado
    print("Consumo energético registrado:", consumo, "kWh")
    return consumo


# ======================================================
# Programa principal
# ======================================================

print("Sistema de Control de Temperatura del Edificio")

# Leer temperatura del sensor
temperatura_actual = leer_temperatura()

# Calcular temperatura óptima
temperatura_optima = calcular_temperatura_optima(temperatura_actual)

# Ajustar sistema de climatización
ajustar_climatizacion(temperatura_optima)

# Registrar consumo energético
registrar_consumo()