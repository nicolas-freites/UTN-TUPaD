#Trabajo Práctico 1 - PRogramación 1
#Alumno - Nicolás Freites.

#1)
print("---Ejercicio 1---") #Imprimimos texto.
print("Hola mundo!") #Imprimimos el texto.

#2)
print("---Ejercicio 2---") #Imprimimos texto.
nombre = input ("Ingrese su nombre: ") #Creamos la variable y hacemos que el usuario escriba su nombre.

print(f"Hola {nombre}!") #Imprimimos el saludo usando f-string.

#3)
print("---Ejercicio 3---") #Imprimimos texto.
nombre = input("Ingrese su nombre: ") #Pide un nombre.
apellido = input ("Ingrese su apellido: ") #Pide un apellido.
edad = input ("Ingrese su edad: ") #Pide la edad.
residencia = input ("Ingrese su lugar de residencia: ") #Pide la residencia.

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")  #Pide todos los anteriores valores concatenando.

#4)
print ("---Ejercicio 4---") #Imprime texto.
radio = float(input("Ingrese el radio del círculo: ")) #Usamos float porque el radio puede tener Decimales.

#Calculamos.
pi = 3.14 #Aclaramos el valor de Pi
area = pi * (radio ** 2) #Elevamos radio a la 2.
perimetro = 2 * pi * radio #Multiplicamos el périmetro.

print (f"El área es : {area}  ") #Imprimimos area
print (f"El perímetro es: {perimetro} ") #Imprimimos perimetro.

#5)
print("---Ejercicio 5---") #Imprime texto.
segundos = int(input("Ingrese una cantidad de segundos: ")) #Pedimos al usuario que ingrese los segundos.

#Calculamos.
horas_totales = segundos/3600 #Lo dividimos por 3600 ya que es el resultado de 60  seg x 60 min.

print(f"La cantidad de horas totales son: {horas_totales:.2f} hora/s") #Imprimimos el resultado (el 2f es para que devuelva decimales.).

#6)
print("---Ejercicio 6---") #Imprimimos texto.
numero = int(input("Ingrese un numero: "))#El usuario ingresa el número.

#Calculamos y mostramos.
print (f"{numero} x 1 = {numero * 1}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 10 = {numero * 10}")

#7)
print("---Ejercicio 7---") #Imprimimos texto.
num1 = int (input("Ingrese un número distinto al 0 : "))
num2 = int(input("Ingrese otro número distinto al 0 : "))

#Calculamos
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

#Imprimimos
print (f"La suma de los dos números es: {suma}")
print (f"La resta de los dos  números es: {resta}")
print (f"La Multiplicación de los dos números es: {multiplicacion}")
print (f"La división de los dos números es: {division:.2f}")

#8)
print("---Ejercicio 8---")

#Le pedimos al  usuario.
altura = float(input("Ingrese su altura en metros : "))
peso = float(input("Ingrese su peso en kg: "))

#Calculamos.
indice = peso / (altura ** 2)

#Imprimimos
print (f"El índice de la masa corporal es: {indice:.2f} ")

#9)
#Imprimimos.
print("---Ejercicio 9---")

#Le pedimos datos al usuario.
celsius = int(input("Ingrese una temperatura en grados Celsius: "))

#Calculamos.
fahrenheit = (9 / 5 * celsius) +32

#Imprimimos la devolución.
print(f"La equivalencia en grados Fahrenheit es: {fahrenheit:.2f}")

#10)
#Imprimimos
print("---Ejercicio 10---")

#Le pedimos datos al usuario.
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

#Calculamos.
promedio = (n1 + n2 + n3) / 3

#Imprimimos el resultado.
print(f"El promedio de los tres números es: {promedio:.2f}")




