#Trabajo Práctico 6 - Funciones
#Alumno: Nicolás Freites

#1)
print("--- Ejercicio 1 ---")

#Definimos la funcion "imprimir_hola_mundo"
def imprimir_hola_mundo():
    print("Hola Mundo!") #Generamos que al llamar dicha función se imprima el texto.

imprimir_hola_mundo() #Hacemos que el programa lo ejecute.

print("\n")

#2)
print("--- Ejercicio 2 ---")

#Creamos función.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Le pedimos el nombre al usuario.
nombre = input("Ingrese su nombre: ")

#Llamamos a la función.
saludo = saludar_usuario(nombre)

#Imprimimos el resultado.
print(saludo)

print("\n")

#3)
print("--- Ejercicio 3 ---")

#Creamos función.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Pedimos los datos necesarios al usuario.
nombra = input("Ingrese su nombre: ")
apellido = input("Ingrese  su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su ciudad: ")

#Llamamos a la función para que Python reemplace los parámetros por valores.
informacion_personal(nombre, apellido, edad, residencia)

print("\n")

#4)
print("--- Ejercicio 4 ---")

#Importamos el módulo matemático.
import math

#Creamos la función del área.
def calcular_area_circulo(radio):
    return math.pi* radio**2

#Creamos la función del perímetro.
def calcular_perimetro_circulo(radio):
    return 2 * math.pi *radio

#Le pedimos al usuario que ingrese el radio.
radio = float(input("Ingrese el radio: "))

#Llamamos a las funciones.
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

#Mostramos los resultados.
print("Área: ", area)
print("Perímetro: ", perimetro)

print("\n")

#5)
print("--- Ejercicio 5 ---")

#Creamos la función.
def segundos_a_horas(segundos):
    return segundos / 3600

#Pedimos los segundos al usuario.
segundos = int(input("Ingrese la cantidad de segundos: "))

#Llamamos a la función.
horas = segundos_a_horas(segundos)

#Mostramos resultado.
print ("Horas: ", horas)

print("\n")

#6)
print("--- Ejercicio 6 ---")

#Creamos una función con un for para repetir x10.
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i }")

#Le pedimos un número al usuario.
numero = int(input("Ingrese un número: "))

#Llamamos a la función.
tabla_multiplicar(numero)

print("\n")

#7)
print("--- Ejercicio 7 ---")

# Creamos la función.
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

# Le pedimos al usuario los números.
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Llamamos a la función.
suma, resta, multiplicacion, division = operaciones_basicas(a,b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("\n")

#8)
print("--- Ejercicio 8 ---")

#Creamos la función.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Pedimos datos al usuario.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura por metros: "))

#Llamamos a la función.
imc = calcular_imc(peso, altura)

#Mostramos el resultado con dos decimales.
print(f"Su IMC es: {imc:.2f}")

print("\n")

#9)
print("--- Ejercicio 9 ---")

#Creamos una función que reciba una temperatura en Celsius y devuelva la temperatura aen Fahrenheit.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Le pedimos la temperatura al usuario.
celsius = float(input("Ingrese la temperatura en Celsius: "))

#Llamamos a la función.
fahrenheit = celsius_a_fahrenheit(celsius)

#Imprimimos resultado.
print("Temperatura en Fahrenheit:", fahrenheit)

print("\n")

#10)
print("--- Ejercicio 10 ---")

#Creamos función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Le pedimos los números al usuario.
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

#Llamamos a la función.
promedio = calcular_promedio(a, b, c)

#Imprimimos resultado.
print("El promedio es:", promedio)

print("\n")