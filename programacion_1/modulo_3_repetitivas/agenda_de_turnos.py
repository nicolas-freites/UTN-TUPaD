print("Ejercicio 3 - Agenda de Turnos.")
#Base de datos, creando una variable única para cada turno.
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

#Validamos al operador.
operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha(): #isalpha para asegurar que sólo tenga letras.
    print("Error: El nombre sólo debe contener letras.")
    operador = input("Ingrese nombre del operador: ")

#Generamos un bucle para el menú principal.
opcion = ""
while opcion != "5":
    print("Menú de Turnos")
    print("1. Reservar turno | 2. Cancelar | 3. Ver Agenda | 4. Resumen | 5. Salir")

    opcion = input("Seleccione una opción: ")

    #Validamos la entrada para evitar que el programa falle con letras o números fuera de rango.
    while not opcion.isdigit() or not ("1" <= opcion <= "5"):
        print("Error: Opción inválida.")
        opcion = input("Seleccione una opción: ")
    
    #Opción 1: Generamos las opciones al reservar.
    if opcion == "1":
        dia = input ("Elija día (1= Lunes, 2= Martes):")
        #Generamos una validación para asegurarnos que el día sea correcto.
        while dia not in ["1", "2"]:
            dia = input("Error. Elija 1 o 2: ")
        
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente= input("Error. Nombre sólo con letras: ")
        
        if dia == "1": #Gestionamos el Lunes.
            #Primero verificamos si el nombre ya existe en alguna de las 4 variables del dia.
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El Paciente ya tiene turno este día.")
                #Si no te repite buscamos la primera variable vacía.
            elif lunes1 == "": lunes1 = paciente; print("Asignado a Turno 1")
            elif lunes2 == "": lunes2 = paciente; print("Asignado a Turno 2")
            elif lunes3 == "": lunes3 = paciente; print("Asignado a Turno 3")
            elif lunes4 == "": lunes4 = paciente; print("Asignado a Turno 4")
            else: print("Día Lunes sin cupos disponibles.")

        else: #Gestionamos el Martes.
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El Paciente ya tiene turno ese día.")
            elif martes1 == "": martes1 = paciente; print("Asignado a Turno 1")
            elif martes2 == "": martes2 = paciente; print("Asignado a Turno 2")
            elif martes3 == "": martes3 = paciente; print("Asignado a Turno 3")
            else: print("Día Martes sin cupos disponibles.")
    
    #Opción 2: Generamos las opciones para Cancelar.
    elif opcion == "2":
        dia = input ("Día para cancelar (1= Lunes, 2= Martes): ")
        paciente = input("Nombre del paciente a borrar: ")

        encontrado = False #Ponemos una Bandera para avisaar que si pudimos borrar al paciente.
        if dia =="1":
            #Si el nombre coincide con la variable, la restamos.
            if lunes1 == paciente: lunes1 = ""; encontrado = True
            elif lunes2 == paciente: lunes2 = ""; encontrado = True
            elif lunes3 == paciente: lunes3 = ""; encontrado = True
            elif lunes4 == paciente: lunes4 = ""; encontrado = True
        else:
            if martes1 == paciente: martes1 = ""; encontrado = True
            elif martes2 == paciente: martes2 = ""; encontrado = True
            elif martes3 == paciente: martes3 = ""; encontrado = True
        
        if encontrado: print(f"Turno de {paciente} cancelado  correctamente.")
        else: print("No se encontró ningún turno a ese nombre.")
    
    #Opción 3: Generamos una Agenda del día.
    elif opcion == "3":
        dia = input("Ver agenda de (1= Lunes, 2= Martes): ")
        if dia == "1":
            #Usamos el 'Or' para que si la vaariable es "" muestre (Libre).
            print(f"Lunes - T1:{lunes1 or '(libre)'}, T2:{lunes2 or '(libre)'}, T3:{lunes3 or '(libre)'}, T4:{lunes4 or '(libre)'}")
        else:
            print(f"Martes - T1:{martes1 or '(libre)'}, T2:{martes2 or '(libre)'}, T3:{martes3 or '(libre)'}")

    #Opción 4: Generamos un resumen.
    elif opcion == "4":
        #Contamos cuántas variables no están vacías para saber los ocupados.
        occ_lunes = (1 if lunes1 else 0) + (1 if lunes2 else 0) + (1 if lunes3 else 0) + (1 if lunes4 else 0)
        occ_martes = (1 if martes1 else 0) + (1 if martes2 else 0) + (1 if martes3 else 0)

        print(f"Resumen Lunes: {occ_lunes} ocupados / {4-occ_lunes} libres")
        print(f"Resumen Martes: {occ_martes} ocupados / {3-occ_martes} libres")

        #Comparación de mayor/menor para determinar el día más concurrido.
        if occ_lunes > occ_martes : print ("El día con más turnos es el Lunes. ")
        elif occ_martes > occ_lunes : print ("El día con más turnos es el Martes.")
        else: print("Ambos días tienen la misma ocupación.")

print(f"Sistema cerrado. Operador Responsable: {operador}")
print("\n")  #Salto de linea con fines estéticos.