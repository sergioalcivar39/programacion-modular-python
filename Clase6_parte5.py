# ======================================================
# Problema 5: Sistema de Riego Automatizado
# ======================================================

# Función para leer datos de sensores de humedad del suelo
def leer_humedad_suelo():
    """
    Lee el nivel de humedad del suelo desde sensores nosotros ingresamos el dato.
    """
    humedad = float(input("Ingrese humedad del suelo (%): "))
    return humedad


# Función para consultar previsión meteorológica
def consultar_clima():
    """
    Consulta si se espera lluvia.
    """
    clima = input("¿Se espera lluvia? (si/no): ")
    return clima


# Procedimiento para calcular la cantidad óptima de riego
def calcular_riego(humedad, clima):
    """
    Determina si es necesario regar el cultivo mediante un blucle if.
    """
    if humedad < 40 and clima == "no":
        agua = 10
        print("Se necesitan", agua, "litros de agua por sector")
        return agua
    else:
        print("No es necesario regar ahora.")
        return 0


# Función para controlar las válvulas de riego
def controlar_valvulas(cantidad_agua):
    """
    Activa o desactiva las válvulas de riego.
    """
    if cantidad_agua > 0:
        print("Abriendo válvulas de riego...")
    else:
        print("Válvulas cerradas.")


# ======================================================
# Programa principal
# ======================================================

# Se llaman a las funciones anteriormente establecidas

print("Sistema de Riego Automatizado")

humedad = leer_humedad_suelo()

clima = consultar_clima()

agua = calcular_riego(humedad, clima)

controlar_valvulas(agua)