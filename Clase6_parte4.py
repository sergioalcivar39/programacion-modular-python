# ======================================================
# Problema 4: Optimización de Producción en una Fábrica
# ======================================================

# Función para monitorear el estado de las máquinas
def monitorear_maquinas():
    """
    Lee el estado de una máquina de producción.
    """
    estado = input("Ingrese estado de la máquina (operativa/falla): ")
    return estado


# Procedimiento para planificar mantenimiento
def planificar_mantenimiento(estado):
    """
    Programa mantenimiento si la máquina presenta fallas.
    """
    if estado == "falla":
        print("Programando mantenimiento preventivo...")
    else:
        print("Máquina funcionando correctamente.")


# Función para analizar rendimiento de producción
def analizar_rendimiento():
    """
    Calcula el porcentaje de eficiencia de producción.
    """
    produccion = int(input("Ingrese cantidad producida hoy: "))
    objetivo = int(input("Ingrese objetivo de producción: "))

    eficiencia = (produccion / objetivo) * 100

    print("Eficiencia de producción:", eficiencia, "%")
    return eficiencia


# Procedimiento para ajustar programación
def ajustar_programacion(eficiencia):
    """
    Ajusta la planificación según el rendimiento.
    """
    if eficiencia < 80:
        print("Aumentar recursos o turnos de producción.")
    else:
        print("Producción dentro de parámetros normales.")


# ======================================================
# Programa principal
# ======================================================

print("Sistema de Optimización de Producción")

estado_maquina = monitorear_maquinas()

planificar_mantenimiento(estado_maquina)

eficiencia = analizar_rendimiento()

ajustar_programacion(eficiencia)