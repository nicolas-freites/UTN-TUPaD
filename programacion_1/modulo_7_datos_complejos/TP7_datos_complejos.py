#Trabajo práctico 7: Estructuras de datos complejas.
#Alumno: Nicolás Freites.

#1)
print("--- Ejercicio 1 ---")

#Diccionario inicial
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

#Agregamos nuevas frutas.
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Nos fijamos el resultado.
print(precios_frutas)

print("\n")

#2)
print("--- Ejercicio 2 ---")

#Actualizamos los precios.
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

print("\n")

#3)
print("--- Ejercicio 3 ---")

#Extraemos las frutas como listas.
frutas = list(precios_frutas.keys())

print(frutas)

print("\n")

#4)
print("--- Ejercicio 4 ---")

#Cargamos 5 contactos.
contactos = {}

for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número: ")
    contactos[nombre] = numero

#Ahora consultamos un contacto.
nombre_buscar = input("Ingresá el nombre a buscar: ")
resultado = contactos.get(nombre_buscar) #.get para verificar si el nombre existe.

if resultado:
    print(f"El número de {nombre_buscar} es: {resultado}")
else:
    print(f"El contacto {nombre_buscar} no existe.")

print("\n")

#5)
print("--- Ejercicio 5 ---")

#Le pedimos al usuario.
frase = input("Ingresá una frase: ")

#Convertimos la frase en lista de palabras.
palabras = frase.split() #Split para separar la frase en palabras.

#Set para palabras únicas.
palabras_unicas = set(palabras)

#Generamos diccionario para contar frecuencias.
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

#Imprimimos.
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

print("\n")


#6)
print("--- Ejercicio 6 ---")

#Cargamos 3 alumnos.
alumnos = {}

for i in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    nota1 = int(input("Ingresá la nota 1: "))
    nota2 = int(input("Ingresá la nota 2: "))
    nota3 = int(input("Ingresá la nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

#Imprimimos el promedio de cada alumno.
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio {promedio:.1f}")

print("\n")

#7)
print("--- Ejercicio 7 ---")

#Lista original con repetidos.
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]

#Lista original.
print(f"Lista original: {asistencias}")

#Set de empleados únicos.
empleados_unicos = set(asistencias)
print(f"Empleados que asistieron al menos una vez: {empleados_unicos}")

#Hacemos el conteo de asistencias por empleado.
conteo = {}
for empleado in asistencias:
    if empleado in conteo:
        conteo[empleado] += 1
    else:
        conteo[empleado] = 1

#Imprimimos.
print(f"Asistencias por empleado: {conteo}")

print("\n")

#8)
print("--- Ejercicio 8 ---")

#Diccionario inicial.
stock = {"Manzana": 50, "Banana": 30, "Naranja": 20}

#Le pedimos al usuario el producto a consultar o agregar.
producto = input("Ingresá el nombre del producto: ")

#Verificamos si el producto existe en el diccionario.
if producto in stock:
    accion = input(f"{producto} existe. ¿Querés consultar el stock o agregar unidades? (consultar/agregar): ")
    
    #Consultamos el stock actual.
    if accion == "consultar":
        print(f"Stock de {producto}: {stock[producto]} unidades.")
    
    #Agregamos unidades al stock existente.
    elif accion == "agregar":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Stock actualizado. {producto}: {stock[producto]} unidades.")

#Si no existe lo creamos como un producto nuevo.
else:
    cantidad = int(input(f"{producto} no existe. ¿Con qué stock inicial lo agregamos?: "))
    stock[producto] = cantidad
    print(f"{producto} agregado con {cantidad} unidades.")

print("\n")

#9)
print("--- Ejercicio 9 ---")

#Diccionario con tuplas como claves.
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Consulta médica",
    ("jueves", "18:00"): "Gimnasio",
    ("viernes", "11:00"): "Entrevista"
}

#Consultamos al usuario qué actividad hay en un día y que hora.
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (formato 00:00): ")

#Buscamos la tupla en el ddiccionario.
resultado = agenda.get((dia, hora))

#Imprimimos el resultado.
if resultado:
    print(f"El {dia} a las {hora} tenés: {resultado}")
else:
    print(f"No hay ningún evento el {dia} a las {hora}.")

print("\n")

#10)
print("--- Ejercicio 10 ---")

#Diccionario original.
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Uruguay": "Montevideo", "Perú": "Lima"}

#Invertimos el diccionario.
invertido = {}
for pais, capital in original.items(): #.items para  recorrer clave y valor al mismo tiempo.
    invertido[capital] = pais

#Imprimimos ambos diccionarios.
print(f"Original: {original}")
print(f"Invertido: {invertido}")

print("\n")