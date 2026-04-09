print("Ejercicio 2 - Acceso al Campus y Menú Seguro")

# Intentos.
intentos = 1
login = False

while intentos <= 3 and not login:
    # Agregamos la 'f' aquí para que funcione la variable
    user = input(f"Intento {intentos}/3 - Usuario: ")
    password = input("Contraseña: ")

    if user == "alumno" and password == "python123":
        login = True
    else: 
        print("Credenciales Inválidas.")
        intentos += 1

# Ingreso al Campus.
if login:
    print("\nAcceso Concedido.")

    # Menú
    opcion = ""
    while opcion != "4":
        print("\n1. Estado.")
        print("2. Cambiar Clave.")
        print("3. Mensaje.")
        print("4. Salir.")

        opcion = input("Seleccione una opción: ")

        # Validación.
        while not opcion.isdigit() or not ("1" <= opcion <= "4"):
            if not opcion.isdigit():    
                print("Error: Ingrese un número válido.") 
            else:
                print("Error: Opción fuera de rango.")
            
            opcion = input("Seleccione una opción: ")

        # Ejecución.
        if opcion == "1":
            print("Estado: Usted se encuentra inscripto en la TUP.")

        elif opcion == "2":
            nueva_clave = input("Ingrese nueva clave (Minimo 6 caracteres): ")
            while len(nueva_clave) < 6:
                print("Error: La clave es demasiado corta.")
                nueva_clave = input("Ingrese nueva clave (mínimo 6): ")
            print("Clave actualizada con éxito.")
        
        elif opcion == "3":
            print("Mensaje: 'Existen dos tipos de personas: Los que dicen 'No puedo' y los que dicen 'Si puedo' y ámbos tienen razón.' ")
        
        elif opcion == "4":
            print("Cerrando sesión... ¡Hasta luego!")
    
else:
    print("\nCuenta bloqueada. Contacte a soporte.")
print("\n")  #Salto de linea con fines estéticos.