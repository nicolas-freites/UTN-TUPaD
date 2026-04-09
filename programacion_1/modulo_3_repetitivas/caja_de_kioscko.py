print("Ejercicio 1 - Caja del Kiosco")

#Caja
total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0

#Pedir el nombre del Cliente.
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Cliente: ")

#Pedir cantidad de productos.
entrada_cant = input("Cantidad de productos: ")
while not entrada_cant.isdigit() or int (entrada_cant) <= 0:
    print("Error: Ingrese un número entero mayor a 0. ")
    entrada_cant = input("Cantidad de productos: ")

cantidad = int(entrada_cant)

#Productos.
for i in range(1, cantidad + 1):
    print(f"Producto {i}")
    
    #Pedir precio
    precio_str = input("Precio: ")
    while not precio_str.isdigit():
        print("Error: Ingrese su número entero para el precio.")
        precio_str = input("Precio: ")
    
    precio = int(precio_str)
    total_sin_descuentos += precio

    #Perdir si tiene descuento.
    descuento_opc = input("Descuento (S/N): ").lower()

    #Si tiene descuento aplicamos el 10%.
    if descuento_opc == "s":
        monto_descuento = precio * 0.10
        ahorro_total += monto_descuento
        precio_final = precio -monto_descuento
    else:
        precio_final = precio
    
    total_con_descuentos += precio_final

#Mostramos los resultados.
promedio = float(total_con_descuentos / cantidad)

print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio  por producto: ${promedio:.2f}")
print("\n")