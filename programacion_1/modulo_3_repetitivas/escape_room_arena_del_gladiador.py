print("Ejercicio 5: Escape Room - La Arena del Gladiador.")

print("---Bienvendio a la Arena---")
#Configuramos al personaje.
nombre = input("Nombre del Gladiador: ")
#Validación para que solo sean letras.
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

#Generamos la base de las estádisticas.
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo = 12
juego_activo = True #Boolean para controlar el ciclo principal.

print("\n=== INICIO DEL COMBATE ===")

#Inicializamos el combate.
while vida_jugador > 0 and vida_enemigo > 0:
    #Mostramos el estado actual.
    print (f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo})| Pociones: {pociones}")
    print("Elige acción: ")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    #Validamos las opciones.
    opcion = input ("Opción: ")
    while not opcion.isdigit() or not  ("1" <= opcion <= "3"):
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Opción fuera de rango (1 - 3).")
            opcion = input("Opción: ")
        
    
    #Generamos las acciones del jugador.
    if opcion == "1":
        #Araque Pesado.
        dmg_final = float(ataque_pesado_base)

        #Si el enemigo tiene menos de 20 HP se le aplicará un golpe crítico.
        if vida_enemigo < 20:
            dmg_final = ataque_pesado_base * 1.5
            print  (f"Golpe Crítico! El daño se multiplica.")

        vida_enemigo = int(dmg_final)
        print(f"Atacaste al enemigo por {dmg_final} puntos de daño! ")
    
    elif opcion == "2":
        #Ráfaga Veloz (Usamos for)
        print(">>> Inicias una Ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conenctado por 5 de daño!")
        
    elif opcion == "3":
        #Curar.
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: #Limite de vida.
                vida_jugador = 100
            pociones -= 1
            print(f"Te curaste! Vida actual: {vida_jugador}. Pociones restantes: {pociones}")
        else:
            print("No te quedan más pociones! Perdés el turno intentando buscar una.")
    
    #Turno del enemigo.
    #El enemigo sólo va atacar si sigue vivo después de que accione el jugador.
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo
        print(f"El Enemigo te atacó por {ataque_enemigo} Puntos de daño!")

#Fin del juego.
print("\n" + "===" * 10)
if vida_jugador > 0:
    print(f"Victoria! {nombre} ha ganado la batalla.")
else:
    print("Derrota. Has caído en combate.")
print("==="* 10)