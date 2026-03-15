    # ======================================================
# Problema 2: Gestión de Inventario en un Almacén
# ======================================================

# Inventario inicial comenzamos con unos datos fijos
inventario = {
    "arroz": 50,
    "azucar": 30,
    "leche": 20
}


# Función para registrar entrada de productos se modifican los valores de los productos del inventario
def registrar_entrada(producto, cantidad):
    """
    Aumenta la cantidad de un producto en el inventario.
    """
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

    print("Entrada registrada:", producto, "+", cantidad)


# Función para registrar salida de productos
def registrar_salida(producto, cantidad):
    """
    Reduce la cantidad de un producto del inventario.
    """
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print("Salida registrada:", producto, "-", cantidad)
    else:
        print("No hay suficiente inventario de", producto)


# Procedimiento para calcular nivel óptimo de inventario
def calcular_nivel_optimo():
    """
    Calcula el nivel promedio de inventario.
    """
    total = sum(inventario.values())
    cantidad_productos = len(inventario)
    # redorderis el termino len sirve cuando usamos arreglos o similares, nos da el total de elementos dentro
    # del arreglo por ejemplo [1,2,3] len 3
    nivel_optimo = total / cantidad_productos

    print("Nivel óptimo promedio de inventario:", nivel_optimo)
    return nivel_optimo


# Función para generar alertas de reabastecimiento
def alerta_reabastecimiento():
    """
    Genera una alerta si algún producto tiene poco inventario.
    """
    for producto, cantidad in inventario.items():
        if cantidad < 10:
            print("ALERTA: Reabastecer", producto)


# ======================================================
# Programa principal
# ======================================================

print("Sistema de Gestión de Inventario")

# Registrar movimientos
registrar_entrada("arroz", 20)
registrar_salida("leche", 5)
# En esta ultima parte llamo a mis funciones anteriormente creadas 
# Calcular nivel óptimo
calcular_nivel_optimo()

# Verificar alertas
alerta_reabastecimiento()

# Mostrar inventario final
print("Inventario actual:", inventario)