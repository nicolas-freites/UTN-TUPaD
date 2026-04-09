#TP1: Estructuras Condicionales.
#Alumno: Nicolás Freites.
# ==========================================

#1)
print("---Ejercicio 1---")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")
print("\n")

#2)
print("---Ejercicio 2---")
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")
print("\n")

#3)
print("---Ejercicio 3---")
numero = int(input("Ingrese un número par: "))

if numero %2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par.")
print("\n")

#4)
print("---Ejercicio 4---")
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Categoría: Niño/a.")
elif edad >= 12 and edad <18:
    print ("Categoría: Adolescente.")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven.")
else:
    print("Categoría: Adulto/a")
print("\n")

#5)
print("---Ejercicio 5---")
password = input("Ingrese su contraseña: ")
largo = len(password)
if largo >= 8 and largo <= 14:
    print("Ha  ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
print("\n")

#6)
print("---Ejercicio 6---")
consumo = float(input("Ingrese el consumo mensual en kwh: "))

if consumo <150:
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético.")
print("\n")

#7)
print("---Ejercicio 7---")
frase = input("Ingrese una frase o palabra: ")

vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

if frase.endswith(tuple(vocales)):
    print(frase + "!")
else:
    print(frase)
print("\n")

#8)
print("---Ejercicio 8---")
nombre = input("Ingrese su nombre: ")

print("Opciones disponibles: ")
print("1. Mostrar en MAYÚSCULAS")
print("2. Mostrar en minúsculas")
print("3. Mostrar con la primera letra en Mayúscula")

opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida.")
print("\n")

#9)
print("---Ejercicio 9 ---")
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
else:
    print("Extremo.")
print("\n")

#10)
print("---Ejercicio 10---")
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia  <=20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

if hemisferio == "S":
    if estacion_norte == "Invierno":
        estacion_final = "Verano"
    elif estacion_norte == "Primavera":
        estacion_final = "Otoño"
    elif estacion_norte == "Verano":
        estacion_final = "Invierno"
    else:
        estacion_final = "Primavera"
else:
    estacion_final = estacion_norte 
print(f"Usted se encuentra en: {estacion_final}")
print("\n")
