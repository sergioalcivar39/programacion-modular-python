# ======================================================
# Sistema Básico de Gestión de Inventario y Pedidos
# Tema: Arreglos unidimensionales
# ======================================================

# Listas que funcionarán como nuestros arreglos
inventario = []
pedidos = []


# ======================================================
# FUNCIONES INVENTARIO
# ======================================================

def registrar_producto():
    """Registra un nuevo producto en el inventario"""

    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)

    print("Producto registrado correctamente\n")


def mostrar_productos():
    """Muestra todos los productos del inventario"""

    if len(inventario) == 0:
        print("No hay productos en el inventario\n")
        return

    print("\nInventario actual")

    for i, producto in enumerate(inventario):
        print(i, producto["nombre"], producto["cantidad"], producto["precio"])

    print()


def editar_producto():
    """Permite editar un producto existente"""

    mostrar_productos()

    if len(inventario) == 0:
        return

    indice = int(input("Seleccione el índice del producto a editar: "))

    nombre = input("Nuevo nombre: ")
    cantidad = int(input("Nueva cantidad: "))
    precio = float(input("Nuevo precio: "))

    inventario[indice]["nombre"] = nombre
    inventario[indice]["cantidad"] = cantidad
    inventario[indice]["precio"] = precio

    print("Producto actualizado\n")


def eliminar_producto():
    """Elimina un producto del inventario"""

    mostrar_productos()

    if len(inventario) == 0:
        return

    indice = int(input("Seleccione el índice del producto a eliminar: "))

    inventario.pop(indice)

    print("Producto eliminado\n")


# ======================================================
# FUNCIONES PEDIDOS
# ======================================================

def registrar_pedido():
    """Registra un nuevo pedido"""

    producto = input("Producto solicitado: ")
    cantidad = int(input("Cantidad: "))

    pedido = {
        "producto": producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)

    print("Pedido registrado\n")


def mostrar_pedidos():
    """Muestra todos los pedidos"""

    if len(pedidos) == 0:
        print("No hay pedidos registrados\n")
        return

    print("\nPedidos actuales")

    for i, pedido in enumerate(pedidos):
        print(i, pedido["producto"], pedido["cantidad"])

    print()


def editar_pedido():
    """Edita un pedido"""

    mostrar_pedidos()

    if len(pedidos) == 0:
        return

    indice = int(input("Seleccione el índice del pedido: "))

    producto = input("Nuevo producto: ")
    cantidad = int(input("Nueva cantidad: "))

    pedidos[indice]["producto"] = producto
    pedidos[indice]["cantidad"] = cantidad

    print("Pedido actualizado\n")


def eliminar_pedido():
    """Elimina un pedido"""

    mostrar_pedidos()

    if len(pedidos) == 0:
        return

    indice = int(input("Seleccione el índice del pedido a eliminar: "))

    pedidos.pop(indice)

    print("Pedido eliminado\n")


# ======================================================
# MENÚ DEL SISTEMA
# ======================================================

def mostrar_menu():

    print("=================================")
    print("Sistema de Inventario y Pedidos")
    print("=================================")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Registrar pedido")
    print("6. Mostrar pedidos")
    print("7. Editar pedido")
    print("8. Eliminar pedido")
    print("0. Salir")


# ======================================================
# PROGRAMA PRINCIPAL
# ======================================================

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        editar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        registrar_pedido()

    elif opcion == "6":
        mostrar_pedidos()

    elif opcion == "7":
        editar_pedido()

    elif opcion == "8":
        eliminar_pedido()

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida\n")