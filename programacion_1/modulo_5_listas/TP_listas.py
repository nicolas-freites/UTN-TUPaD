#Trabajo Práctico - Listas - Programación 1
#Alumno - Nicolás Freites.

#1) Crear una lista con las notas de 10 estudiantes.
print("---Ejercicio 1---")

#Usamos una lista de enteros.
notas = [8, 9, 4, 10, 7, 6, 8, 5, 10, 7]

#Mostramos la lista completa usando repetitivas.
print("---Listado de Notas---")

for i in range(len(notas)):
    #Imprimimoss el índice + 1 para que sea legible.
    print(f"Estudiante {i + 1}: {notas[i]}")

#Calculamos y mostramos el promedio.
suma_total = 0
#Recorremos la lista sumando cada nota al acumulador.
for nota in notas:
    suma_total += nota

#Sacamos el promedio de la suma total de la cantidad de elementos.
promedio = suma_total / len(notas)
print(f"\nPromedio del curso: {promedio}")

#Indicamos la nota más alta y más baja usando funciones integradas max y min.
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"La nota más alta alcanzada fue: {nota_maxima}")
print(f"La nota más baja alcanzada fue: {nota_minima}")
print("\n") #Espacio estético.

#2) Pedir al usuario que cargue 5 productos en una lista.
print("---Ejercicio 2---")

#Inicializamos una lista vacía para cargar los productos.
productos = []

#Le pedimos al  usuario que carge 5 productos usando un bucle for.
for i in range(5):
    item = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(item) #Usamos append para agregar el elemento al final de la lista.

#Mostramos la lista ordenada alfabéticamente usando sorted.
print("\n---Lista de Productos---")
lista_ordenada = sorted(productos)

#Volvemos a usar un for para mostrar los elementos.
for p in lista_ordenada:
    print(f"-{p}")

#Le preguntamos al usuario que producto desea eliminar.
producto_a_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")

#Antes de intentar borrarlo, se verifica si el producto existe.
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar) #Usamos remove para eliminarlo.
    print(f"El producto {producto_a_eliminar} ha sido eliminado.")
else:
    print("Error: El producto no se encuentra en la lista.")

#Finalizamos mostrando la lista actualizada.
print("\n---Inventario Actualizado---")
if len(productos) == 0:
    print("La lista está vacía.")
else:
    for p in productos:
        print(f"-{p}")
print("\n")

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
print("---Ejercicio 3---")
#Importamos el módulo para generar números aleatorios.
import random 

#Generamos la lista principal.
numeros_azar = []
for i in range(15):
    #Generamos un número entero aleatorio incluyendo los límites.
    numero = random.randint(1, 100)
    numeros_azar.append(numero)

#Generamos listas para pares e impares.
pares = []
impares = []

#Recorremos la lista original y clasificamos.
for n in numeros_azar:
    if n % 2 == 0: 
        pares.append(n) #Si el resto de dividir por 2 es 0, es par.
    else:
        impares.append(n) #De lo contrario, es impar.

#Imprimimos los resultados.
print("---Números generados al Azar---")
for n in numeros_azar:
    print(n)

print("\n--- Lista de Pares ---")
for p in pares:
    print(p) 

# Mostramos cuántos números tiene la lista de pares.
print("Cantidad de números pares:")
print(len(pares))

print("\n--- Lista de Impares ---")
for i in impares:
    print(i) 

# Mostramos cuántos números tiene la lista de impares.
print("Cantidad de números impares:")
print(len(impares))
print("\n")

#4) Dada una lista con valores repetidos:
print("---Ejercicio 4---")

#Definimos la lista con los valores.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#Creamos una lista vacía para guardar los elementos únicos.
sin_repetidos = []

#Buscamos duplicados en la lista original.
for numero in datos:
    #Si el número no está en la lista, lo agregamos.
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

#Imprimimos el resultado.
print("---Lista Original---")
for d in datos:
    print(d)

print("\n--- Lista Sin elementos repetidos ---")
for n in sin_repetidos:
    print(n)
print("\n")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
print("---Ejercicio 5---")
#Creamos una lista con los nombres de los estudiantes.
estudiantes = ["Matias", "Sofia", "Santino", "Valentina", "Joaquín", "Melanie", "Andrea", "Kevin"]

#Mostramos la lista inicial.
print("--- Lista inicial de estudiantes ---")
for nombre in estudiantes:
    print(nombre)

#Le preguntamos al usuario si quiere agregar o  eliminar un estuidiante.
print("\nOpciones de gestión: ")
print("1. Agregar un nuevo estudiante")
print("2. Eliminar un estudiante existente")
opcion = input("Seleccione una opción (1 o 2): ")

#Actualizamos la lista.
if opcion == "1":
    nuevo_nombre = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo_nombre)
    print("Estudiante agregado.")
elif opcion == "2":
    nombre_eliminar = input ("Ingrese el nombre del estudiante a eliminar: ")
    #Verificamos si existe antes de borrarlo.
    if nombre_eliminar in estudiantes:
        estudiantes.remove(nombre_eliminar)
        print("Estudiante eliminado.")
    else:
        print("El nombre no se encuentra en la lista.")
else:
    print("Opción no válida.")

#Imprimimos la lista actualizada.
print("\n--- Lista final actualizada ---")
for nombre in estudiantes:
    print(nombre)
print("\n")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha.
print("---Ejercicio 6---")

#Empezamos definiendo la lista con los números.
numeros = [10, 20, 30, 40, 50, 60, 70]

#Mostramos la lista original.
print("--- Lista Original ---")
for n in numeros:
    print(n)
#Tomamos el último elemento usando  el índice -1
ultimo = [numeros[-1]]

#Tomamos todos los elementos excepto el último.
el_resto = numeros[0:6]

#Creamos nueva lista uniendo las dos partes.
numeros_rotados = ultimo + el_resto

#Imprimimos la lista actualizada.
print("\n=== Lista Rotada ===")
for n in numeros_rotados:
    print(n)
print("\n")

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
print("---Ejercicio 7---")
#Definimos las dimensiones de la matriz.
filas = 7
columnas = 2

#inicializamos la matriz 
matriz_temperaturas = [[0] * columnas for i in range (filas)]

#Carga de datos por parte del usuario.
print("\n--- Ingreso de Datos  Climáticos--- ")
for i in range(len(matriz_temperaturas)):
    print(f"Día{i + 1}:")
    #Usamos float por si las temperaturas tienen decimales.
    matriz_temperaturas[i][0] = float(input("  Ingrese temperatura mínima: "))
    matriz_temperaturas[i][1] = float(input("  Ingrese temperatura máxima: "))

#Mostramos la matriz completa.
print("\n--- Registro Completo ---")
for dia in matriz_temperaturas:
    print(dia)

#Calculamos el promedio de min y max.
suma_minimas = 0
suma_maximas = 0

for dia in matriz_temperaturas:
    suma_minimas += dia [0]
    suma_maximas += dia [1]

promedio_min = suma_minimas / filas
promedio_max = suma_maximas / filas

print(f"\nPromedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")

#Indentificamos  el dia con más amplitud térmica.
max_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(matriz_temperaturas)):
    amplitud_actual = matriz_temperaturas[i][1] - matriz_temperaturas [i][0]

    #Si encontramos una mayor amplitud, actualizamos.
    if amplitud_actual > max_amplitud:
        max_amplitud = amplitud_actual
        dia_mayor_amplitud = i + 1

print(f"\nLa mayor amplitud térmica fue de {max_amplitud} grados, registrada el Día {dia_mayor_amplitud}.")
print("\n")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
print("---Ejercicio 8---")

#Definimos las dimensiones de la matriz
filas = 5
columnas = 3

#Inicializamos la matriz con ceros.
notas = [[0.0] * columnas for i in range(filas)]

#Cargamos los datos.
print("--- Ingreso de notas de estudianates ---")
for i in range(filas):
    print(f"\nNotas del Estudiante {i + 1}:")
    for j in range(columnas):
        notas[i][j] = float(input(f"Materia {j + 1}: "))

#Mostramos la matriz completa.
print("\n--- Cuadro de Notas Completo ---")
for fila in notas:
    print(fila)

#Mostramos el promedio de cada estudiante.
print("\n--- Promedios por Estudiante ---")
for i in range(filas):
    suma_estudiante = 0
    for j in range(columnas):
        suma_estudiante += notas[i][j]
    
    promedio_individual = suma_estudiante / columnas
    print(f"Estudiante {i + 1}: {promedio_individual:.2f}")

#Mostramos el promedio de cada materia.
print("\n--- Promedio por Materia ---")
for j in range(columnas):
    suma_materia = 0
    for i in range (filas):
        #Invertimos.
        suma_materia += notas [i][j]

    promedio_materia = suma_materia / filas
    print(f"Materia {j + 1}: {promedio_materia:2f}")
print("\n")

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
print("---Ejercicio 9---")

#Inicializamos el tablero.
filas = 3
columnas = 3
tablero = [["-"] * columnas for i in range(filas)]

#Juego para dos jugadores.
for turno in range(9):

    #Mostramos el tablero.
    print("\nTablero  Actual: ")
    for fila in tablero:
        print(fila)
    
    #Determinamos el símbolo según el turno.
    if turno % 2 == 0:
        simbolo = "X"
        print("\nTurno del Jugador 1 (X)")
    else:
        simbolo = "O"
        print("\nTurno del Jugador 2 (O)")
    
    #Pedimos las posiciones.
    f = int(input("Ingrese número de fila (1, 2 o 3): ")) - 1
    c = int(input("Ingrese número de columna (1, 2 o 3): ")) - 1

    #Actualizamos el tablero y verificamos si la casilla está vacía.
    if 0 <= f <= 2 and 0 <= c <= 2:
        if tablero[f][c] == "-":
            tablero[f][c] = simbolo
        else:
            print("Posición ocupada. Perdió su turno.")
    else:
        print("Posición fuera del tablero.")

#Mostramos el tablero final.
print("\n--- Estado final del tablero ---")
for fila in tablero:
    print(fila)
print("\n")

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
print("---Ejercicio 10---")

#Inicializamos con los valores.
productos = 4
dias = 7
matriz_ventas = [[0] * dias for i in range(productos)]

#Cargamos los productos.
print("--- Ingreso de Ventas Semanales ---")
for p in range(productos):
    print(f"\nProducto {p + 1}:")
    for d in range(dias):
        matriz_ventas[p][d] = int(input(f"  Ventas del día {d + 1}: "))

#Mostramos el total vendido por cada producto.
print("\n--- Total de Ventas por Producto ---")
totales_por_producto = [] #Usamos una lista para guardar los totales finales de  cada producto.

for p in range(productos):
    suma_producto = 0
    for d in range(dias):
        suma_producto += matriz_ventas[p][d]
    totales_por_producto.append(suma_producto)
    print(f"Producto {p + 1}: {suma_producto} unidades.")
#Mostramos el día con mayores ventas  totales.
print("\n--- Analizando el día con mayores ventas ---")
max_ventas_dia = 0
dia_ganador = 0

for d in range(dias):
    suma_dia = 0
    for p in range(productos):
        suma_dia += matriz_ventas[p][d]
    
    if suma_dia > max_ventas_dia:
        max_ventas_dia = suma_dia
        dia_ganador = d + 1
print(f"El día con mayores ventas fue el Día {dia_ganador} con un total de {max_ventas_dia} unidades.")

#Indicamos cual fue el producto mas vendido de la semana.
max_unidades = 0
producto_ganador = 0

for i in range (len(totales_por_producto)):
    if totales_por_producto[i] > max_unidades:
        max_unidades = totales_por_producto[i]
        producto_ganador = i + 1
print(f"\nEl producto más vendido fue el Producto {producto_ganador} con {max_unidades} unidades.")
print("\n")


#11)  Crear una lista con los nombres de 10 estudiantes. 
print("---Ejercicio 11---")
#Empezamos creando los nombres en la lista.
estudiantes = ["Matias", "Sofia", "Santino", "Valentina", "Joaquín", "Melanie", "Andrea", "Kevin", "Yanina", "Nicolás"]

#Mostramos la lista de alumnos.
print("=== Lista de Estudiantes ===")
for nombre in estudiantes:
    print(nombre)

#Solicitamos al usuario que ingrese un nombre para buscar.
buscar = input("\nIngrese el nombre del estudiante que desea buscar: ")

#Inicializamos variables para controlar la búsqueda.
encontrado = False
posicion = -1

for i in range(len(estudiantes)):
    #Comprobamos el nombre ingresado.
    if estudiantes[i] == buscar:
        encontrado = True
        posicion = i #Guardamos poosición.
        break #Si lo encontramos, termina.
#Resultados.
if encontrado:
    print(f"\nEl estudiante {buscar} se encuentra en la lista.")
    print(f"Aparece en la posición número: {posicion + 1}")
else:
    print(f"\nEl Estudiante {buscar} no se encuentra en la lista.")
print("\n")

#12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
print("---Ejercicio 12---")

# Cargamos los datos.
numeros = []
for i in range(8):
    numeros.append(int(input(f"Ingrese el número {i + 1}: ")))

# Generamos la lista original.
print("\n--- Lista Original ---")
for n in numeros:
    print(n)

# Ordenamos de menor a mayor usando sorted.
lista_menor_a_mayor = sorted(numeros)

print("\n--- De Menor a Mayor ---")
for n in lista_menor_a_mayor:
    print(n)

# Ordenamos de mayor a menor usando sorted con reverse=True.
lista_mayor_a_menor = sorted(numeros, reverse=True)

print("\n--- De Mayor a Menor ---")
for n in lista_mayor_a_menor:
    print(n)
print("\n")

#13) Mostrar puntajes de un videojuego.
print("---Ejercicio 13---")

#Definición de la lista inicial.
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

#Encontramos el puntaje más alto y el más bajo usando funciones integradas.
maximo = max (puntajes)
minimo = min(puntajes)

print(f"Puntaje más alto: {maximo}")
print(f"Puntaje más bajo: {minimo}")

#Creamos el ranking de mayor a menor.
lista_auxiliar = sorted(puntajes)
ranking = []

#Recorremos de atrás para delante asi invertimos el orden manualmente.
for i in range(len(lista_auxiliar) -1, -1, -1):
    ranking.append(lista_auxiliar[i])

print("\n--- Ranking de Puntajes (Mayor a Menor) ---")
for p in ranking:
    print(p)

#Indicamos en que posición está el puntaje 990.
puntaje_buscado = 990
posicion_encontrada = -1

for i in range(len(ranking)):
    if ranking[i] == puntaje_buscado:
        #Guardamos la posición 
        posicion_encontrada = i + 1
        break
print(f"\nEl puntaje {puntaje_buscado} se encuentra en la posición N° {posicion_encontrada} del ranking.")


