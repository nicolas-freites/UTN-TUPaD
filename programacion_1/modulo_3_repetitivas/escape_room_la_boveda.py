print("Ejercicio 4: Escape Room - La Bóveda.")
#Empezamos creando las variables iniciales.
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0 #Variable de control para Anti-spam.

#Validamos al Agente.
agente = input("Ingrese nombre del agente: ")
while not agente.isalpha():
    print("Error: El nombre solo debe contener letras.")
    agente = input("Infrese nonmbre del agente: ")

print(f"\nBienvenido, Agente {agente}. La misión comienza.")

#Generamos el Bucle principal del juego.
# El juego sigue mientras haya energía, tiempo, falten cerraduras y no esté bloqueado por alarma crítica.
while energia > 0 and tiempo > 0 and cerraduras_abiertas <3:

    #Verificación de bloqueo por alarma.
    if alarma == True and tiempo <= 3:
        print("\n¡Sistema Bloqueado! La alarma detectó intrusión crítica.")
        break

    #Estado Actual.
    print(f"\n{'='*30}") #Multiplicamos '=' por 30 para darles lineas de separación estéticas.
    print(f"Estado: Energía: {energia} | Tiempo: {tiempo}h")
    print(f"Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código hackeo: [{codigo_parcial}]")
    print(f"{'='*30}")

    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Acción: ")
    while not opcion.isdigit() or not ("1" <= opcion <= "3"):
        print("Error: Opción Inválida.")
        opcion = input ("Acción: ")

    #Generamos la lógica de acciones.
    if opcion == "1":
        #Costo base.
        energia -= 20
        tiempo -= 2
        racha_forzar += 1 #Aumenta la racha.

        #Regla Anti-Spam (3 Veces seguidas) 
        if racha_forzar == 3:
            alarma = True
            print("La Cerradura se trabó! Anti-Spam activado: Alarma ON.")
        else:
            #Riesgo de alarma por baja energía.
            if energia < 40:
                print("ADVERTENCIA: Bajo nivel de energia. Riesgo de alarma.")
                num_riesgo = input("Elija un número de seguridad (1 - 3): ")
                while not num_riesgo.isdigit() or not ("1" <= num_riesgo <= "3"):
                    num_riesgo = input ("Elija 1, 2 o 3: ")

                if num_riesgo == "3":
                    alarma = True
                    print("Activaste los sensores de movimiento! Alarma ON.")
                
                #Si no saltó la alarma por racha ni por riesgo, abre la cerradura.
            if not alarma:
                    cerraduras_abiertas += 1
                    print("Cerradura forzada con éxito.")
    
    elif opcion == "2":
        #Cortamos la racha de forzar.
        racha_forzar = 0
        energia  -= 10
        tiempo -= 3

        print("Hackeando sistema...")
        #Generamos un Bucle de 4 pasos para el progreso.
        for i in range (1, 5):
            codigo_parcial += "A"
            print(f"Precesando nodo {i}... Código actual: {codigo_parcial}")

        #Verificación automática de apartura por hackeo.
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo Exitoso! El sistema cedió. Cerradura Abierta.")
    
    elif opcion == "3":
        #Cortamos la racha de forzar.
        racha_forzar = 0
        tiempo -= 1

        recuperacion = 15
        if alarma:
            recuperacion -= 10 #Penalización por alarma activada.
            print("Descanso interrumpido por el ruido de la alarma (-10 extra).")

        energia += recuperacion
        if energia > 100: energia = 100 #Establecemos límite máximo.
        print(f"Energía recuperada. Nivel actual: {energia}")

#Finalización.
print("\n" + "#"*30)
if cerraduras_abiertas == 3:
    print(f"Victoria! El Agente {agente} ha abierto la bóveda.")
elif energia <= 0:
    print("Derrota: Te quedaste sin energía. El agente se desmayó.")
elif tiempo <= 0:
    print("Derrota: Se acabó el tiempo. Los refuerzos llegaron.")
else:
    print("Derrota: El sistema se bloqueó permanentemente.")
print("#"*30)
print("\n")  #Salto de linea con fines estéticos.
