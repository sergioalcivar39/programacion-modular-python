# ============================================

# README - RETO 3

# SISTEMA DE INVENTARIO OPTIMIZADO

# ============================================

Autor: Sergio Alcivar
Asignatura: Estructuras de Datos
Tema: Listas enlazadas, pilas y colas (Parte 4)

---

## INTRODUCCIÓN

En este proyecto se optimiza un sistema de gestión de inventario y pedidos mediante el uso de estructuras de datos avanzadas: lista enlazada, cola (queue) y pila (stack).

El objetivo es mejorar la eficiencia en el manejo de productos, pedidos y control de acciones dentro del sistema.

---

## PROBLEMA IDENTIFICADO

En los sistemas básicos de inventario, se presentan limitaciones como:

* Manejo poco eficiente de productos dinámicos
* Procesamiento desordenado de pedidos
* Falta de historial o control de acciones

Para resolver estos problemas, se implementaron estructuras de datos que optimizan cada uno de estos aspectos.

---

## ESTRUCTURAS UTILIZADAS

1. LISTA ENLAZADA (Inventario)

Se utiliza para almacenar los productos disponibles.

Características:

* Estructura dinámica
* No requiere tamaño fijo
* Inserción eficiente

Justificación:
Permite agregar o modificar productos sin necesidad de reorganizar toda la estructura.

---

2. COLA (Pedidos)

Se utiliza para gestionar los pedidos de los clientes.

Características:

* Sigue el principio FIFO (First In, First Out)
* Los pedidos se atienden en orden de llegada

Justificación:
Garantiza equidad en la atención de pedidos, simulando sistemas reales.

---

3. PILA (Historial)

Se utiliza para registrar acciones realizadas en el sistema.

Características:

* Sigue el principio LIFO (Last In, First Out)
* Permite deshacer acciones recientes

Justificación:
Facilita el control del sistema y la reversión de operaciones.

---

## FUNCIONALIDADES IMPLEMENTADAS

* Agregar productos al inventario
* Mostrar inventario actual
* Registrar pedidos de clientes
* Procesar pedidos en orden de llegada
* Reducir stock automáticamente
* Guardar historial de acciones
* Deshacer última acción realizada

---

## EJECUCIÓN DEL PROGRAMA

Para ejecutar el sistema, usar el siguiente comando:

python sistema.py

(Asegúrese de tener Python instalado)

---

## EJEMPLO DE EJECUCIÓN

Producto agregado: Laptop (10)
Producto agregado: Mouse (20)

Pedido agregado: Juan pidió Laptop
Pedido agregado: Ana pidió Mouse

Pedido procesado: Juan
Pedido procesado: Ana

Inventario:
Mouse: 15
Laptop: 8

Deshaciendo: Pedido Ana

---

## ANÁLISIS DE COMPLEJIDAD

Lista enlazada:

* Inserción: O(1)
* Búsqueda: O(n)

Cola:

* Enqueue: O(1)
* Dequeue: O(n) (por uso de lista)

Pila:

* Push: O(1)
* Pop: O(1)

---

## VENTAJAS DEL SISTEMA

✔️ Manejo eficiente de datos dinámicos
✔️ Procesamiento ordenado de pedidos
✔️ Control de acciones mediante historial
✔️ Código modular y organizado

---

## POSIBLES MEJORAS

* Implementar interfaz gráfica
* Usar estructuras más eficientes (deque, heap)
* Validaciones adicionales (stock negativo, entradas inválidas)
* Persistencia de datos (archivos o base de datos)

---

## CONCLUSIÓN

La integración de estructuras de datos avanzadas permite optimizar significativamente el sistema de inventario, mejorando su eficiencia, organización y funcionalidad.

Este enfoque refleja cómo estructuras como listas enlazadas, colas y pilas son fundamentales en el desarrollo de sistemas reales.

---

## FIN DEL DOCUMENTO
