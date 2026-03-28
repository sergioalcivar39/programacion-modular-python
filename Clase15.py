# ============================================
# SISTEMA DE INVENTARIO OPTIMIZADO
# ============================================

# ============================================
# LISTA ENLAZADA (PRODUCTOS)
# ============================================

class NodoProducto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.siguiente = None


class Inventario:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, nombre, cantidad):
        nuevo = NodoProducto(nombre, cantidad)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        print(f"Producto agregado: {nombre} ({cantidad})")

    def mostrar(self):
        actual = self.cabeza
        print("\nInventario:")
        while actual:
            print(f"{actual.nombre}: {actual.cantidad}")
            actual = actual.siguiente

    def reducir_stock(self, nombre, cantidad):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                actual.cantidad -= cantidad
                return True
            actual = actual.siguiente
        return False


# ============================================
# COLA (PEDIDOS)
# ============================================

class Pedido:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad


class ColaPedidos:
    def __init__(self):
        self.cola = []

    def enqueue(self, pedido):
        self.cola.append(pedido)
        print(f"Pedido agregado: {pedido.cliente} pidió {pedido.producto}")

    def dequeue(self):
        if self.is_empty():
            return None
        return self.cola.pop(0)

    def is_empty(self):
        return len(self.cola) == 0


# ============================================
# PILA (HISTORIAL)
# ============================================

class Historial:
    def __init__(self):
        self.pila = []

    def push(self, accion):
        self.pila.append(accion)

    def pop(self):
        if self.is_empty():
            return None
        return self.pila.pop()

    def is_empty(self):
        return len(self.pila) == 0


# ============================================
# SISTEMA PRINCIPAL
# ============================================

class Sistema:
    def __init__(self):
        self.inventario = Inventario()
        self.pedidos = ColaPedidos()
        self.historial = Historial()

    def agregar_producto(self, nombre, cantidad):
        self.inventario.agregar_producto(nombre, cantidad)
        self.historial.push(f"Agregar {nombre}")

    def nuevo_pedido(self, cliente, producto, cantidad):
        pedido = Pedido(cliente, producto, cantidad)
        self.pedidos.enqueue(pedido)

    def procesar_pedido(self):
        pedido = self.pedidos.dequeue()

        if pedido is None:
            print("No hay pedidos")
            return

        if self.inventario.reducir_stock(pedido.producto, pedido.cantidad):
            print(f"Pedido procesado: {pedido.cliente}")
            self.historial.push(f"Pedido {pedido.cliente}")
        else:
            print("Producto no encontrado")

    def deshacer(self):
        accion = self.historial.pop()
        if accion:
            print(f"Deshaciendo: {accion}")
        else:
            print("Nada que deshacer")

    def mostrar(self):
        self.inventario.mostrar()


# ============================================
# PRUEBA DEL SISTEMA
# ============================================

sistema = Sistema()

# inventario
sistema.agregar_producto("Laptop", 10)
sistema.agregar_producto("Mouse", 20)

# pedidos
sistema.nuevo_pedido("Juan", "Laptop", 2)
sistema.nuevo_pedido("Ana", "Mouse", 5)

# procesar pedidos
sistema.procesar_pedido()
sistema.procesar_pedido()

# mostrar inventario
sistema.mostrar()

# deshacer acción
sistema.deshacer()