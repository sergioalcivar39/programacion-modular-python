# ======================================================
# Problema 4: Optimización de Producción en una Fábrica
# ======================================================

# Función para monitorear el estado de las máquinas
def monitorear_maquinas():
    """
    Lee el estado de una máquina de producción aca originalmente esto seguia porque no detectaba las mayusculas 
    # o espacios asi que con el lower lo dejas todo igual y con el otro quitas espacios.
    """
    estado = input("Ingrese estado de la máquina (operativa/falla): ").strip().lower()
    return estado


# Procedimiento para planificar mantenimiento
def planificar_mantenimiento(estado):
    """
    Programa mantenimiento si la máquina presenta fallas.
    """
    if estado == "falla":
        print("Máquina en falla. Programando mantenimiento preventivo...")
        return False
    else:
        print("Máquina funcionando correctamente.")
        return True


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

maquina_operativa = planificar_mantenimiento(estado_maquina)

# Solo analizar producción si la máquina funciona
if maquina_operativa:

    eficiencia = analizar_rendimiento()

    ajustar_programacion(eficiencia)