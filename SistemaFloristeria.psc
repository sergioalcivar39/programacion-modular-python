Algoritmo SistemaFloristeria
	Definir flores Como Cadena
	Definir cantidad Como Entero
	Definir precio Como Real
	Definir pedido, opcion, i Como Entero
	Definir total Como Real
	Dimensionar flores(3)
	Dimensionar cantidad(3)
	Dimensionar precio(3)
	total <- 0
	Escribir '===== Ingreso del inventario ====='
	Para i<-1 Hasta 3 Hacer
		Escribir 'Inserte el nombre de la flor:'
		Leer flores[i]
		Escribir 'Insere la cantidad:'
		Leer cantidad[i]
		Escribir 'Inserte el precio:'
		Leer precio[i]
	FinPara
	Repetir
		Escribir '===== Menu ====='
		Escribir '1. Mostrar inventario'
		Escribir '2. Realizar pedido'
		Escribir '3. Salir'
		Leer opcion
		Si opcion=1 Entonces
			Para i<-1 Hasta 3 Hacer
				Escribir 'Flor: ', flores[i], ' Cantidad: ', cantidad[i], ' Precio: ', precio[i]
			FinPara
		SiNo
			Si opcion=2 Entonces
				Escribir 'Seleccione flor (1-3)'
				Leer pedido
				Si cantidad[pedido]>0 Entonces
					cantidad[pedido] <- cantidad[pedido]-1
					total <- total+precio[pedido]
					Escribir 'Pedido realizado'
					Escribir 'Total a pagar: ', total
				SiNo
					Escribir 'No hay stock disponible'
				FinSi
			FinSi
		FinSi
	Hasta Que opcion=3
	Escribir 'Sistema finalizado'
FinAlgoritmo
