# Programación 1 - Parcial 1.
# Alumno: Nicolás Freites.

# Generamos listas vacías.
herramientas = []
existencias = []

# Bandera para mantener el menú activo.
continuar = True

while continuar:
    print("\n==== Sistema de Inventario ====")
    print("1. Carga inicial de herramientas")
    print("2. Carga de existencias")
    print("3. Visualización de inventario")
    print("4. Consulta de stock")
    print("5. Reporte de agotados")
    print("6. Alta de nuevo producto")
    print("7. Actualización de stock (venta/ingreso)")
    print("8. Salir")

    opcion = input("Elegí una opción: ")

    # Opción 1:  Carga de herramientas.
    if opcion == "1":
        # Vaciamos las listas por si el usuario quiere rehacer la carga.
        herramientas = []
        existencias = []

        # Pedimos la cantidad de herramientas a cargar con validación.
        cantidad_valida = False
        while not cantidad_valida:
            entrada_cantidad = input("¿Cuántas herramientas querés cargar? ")
            if entrada_cantidad.isdigit() and int(entrada_cantidad) > 0:
                cantidad = int(entrada_cantidad)
                cantidad_valida = True
            else:
                print("Error: ingresá un número entero mayor a cero.")

        # Recorremos tantas veces como herramientas haya que cargar.
        for i in range(cantidad):
            nombre_valido = False  # Bandera en False hasta que el nombre sea correcto.

            while not nombre_valido:
                nombre = input(f"Ingresá el nombre de la herramienta {i + 1}: ").strip()

                # Validamos que el nombre no esté vacío.
                if nombre == "":
                    print("Error: el nombre no puede estar vacío.")

                # Validamos que el nombre no esté duplicado.
                else:
                    duplicado = False
                    for nombre_existente in herramientas:
                        if nombre_existente.lower() == nombre.lower():
                            duplicado = True

                    if duplicado:
                        print(f"Error: '{nombre}' ya fue registrado. Ingresá otro nombre.")
                    else:
                        # Nombre válido: lo agregamos a la lista y salimos del while.
                        herramientas.append(nombre)
                        nombre_valido = True

        print(f"\n✓ Se cargaron {len(herramientas)} herramientas correctamente.")

    # Opción 2: Carga de existencias.

    elif opcion == "2":
        # Validamos que haya herramientas cargadas antes de continuar.
        if len(herramientas) == 0:
            print("Error: primero debés cargar las herramientas (opción 1).")

        else:
            # Reseteamos existencias por si el usuario repite la opción.
            existencias = []

            for i in range(len(herramientas)):
                entrada_valida = False  # Aplicamos bandera.

                while not entrada_valida:
                    # Mostramos el nombre de la herramienta actual.
                    print(f"Herramienta: {herramientas[i]}")
                    entrada = input("Ingresá las existencias: ")

                    # Usamos isdigit() para validar: acepta 0 y positivos, rechaza negativos y texto.
                    if entrada.isdigit():
                        existencias.append(int(entrada))
                        entrada_valida = True  # Salimos del while.
                    else:
                        print("Error: ingresá un número entero positivo o cero.")

            print(f"\n✓ Existencias cargadas para {len(existencias)} herramientas.")

    # Opción 3: Visualización de inventario.

    elif opcion == "3":
        # Validación previa: no mostramos nada si las listas están vacías.
        if len(herramientas) == 0:
            print("Error: no hay herramientas cargadas en el sistema.")

        else:
            print("\n===== Inventario Actual =====")
            print(f"{'Herramienta':<20} {'Existencias':>10}") # Detalles estéticos, 20 y 10 caracteres de ancho.
            print("-" * 32) # Aplicamos un separador visual.

            # Recorremos ambas listas por índice para mantener la sincronía.
            for i in range(len(herramientas)):
                print(f"{herramientas[i]:<20} {existencias[i]:>10}")

            print("-" * 32) # Detalle estético.
            print(f"Total de productos: {len(herramientas)}")

    # Opción 4: Consulta de stock.

    elif opcion == "4":
        # Validación previa: no se puede consultar si no hay herramientas cargadas.
        if len(herramientas) == 0:
            print("Error: no hay herramientas cargadas en el sistema.")

        else:
            nombre_buscado = input("Ingresá el nombre de la herramienta a consultar: ").strip()

            encontrado = False  # Bandera de búsqueda.

            for i in range(len(herramientas)):
                if herramientas[i].lower() == nombre_buscado.lower():
                    print(f"\nHerramienta: {herramientas[i]}")
                    print(f"Existencias disponibles: {existencias[i]} unidades.")
                    encontrado = True

            # Si recorrimos toda la lista y no encontramos nada, avisamos.
            if not encontrado:
                print(f"Error: '{nombre_buscado}' no existe en el catálogo.")

    # Opción 5: Reporte de agotados.

    elif opcion == "5":
        # Validación previa: no se puede reportar si no hay herramientas cargadas.
        if len(herramientas) == 0:
            print("Error: no hay herramientas cargadas en el sistema.")

        else:
            print("\n===== Productos Agotados =====")

            hay_agotados = False  # Bandera para saber si encontramos algún agotado.

            for i in range(len(herramientas)):
                # Mostramos solo las herramientas con stock igual a cero.
                if existencias[i] == 0:
                    print(f"- {herramientas[i]}")
                    hay_agotados = True

            # Si no hubo ningún agotado, avisamos.
            if not hay_agotados:
                print("No hay productos agotados en este momento.")

    # Opción 6: Alta de nuevo producto.

    elif opcion == "6":
        nombre_nuevo = input("Ingresá el nombre del nuevo producto: ").strip()

        # Validamos nombre vacío: volvemos al menú con mensaje.
        if nombre_nuevo == "":
            print("Error: el nombre no puede estar vacío.")

        else:
            # Validamos nombre duplicado.
            duplicado = False
            for nombre_existente in herramientas:
                if nombre_existente.lower() == nombre_nuevo.lower():
                    duplicado = True

            if duplicado:
                print(f"Error: '{nombre_nuevo}' ya existe en el catálogo.")

            else:
                stock_nuevo = input("Ingresá el stock inicial del producto: ")

                # Validamos que el stock no sea negativo ni texto.
                if not stock_nuevo.isdigit():
                    print("Error: el stock debe ser un número entero positivo o cero.")

                else:
                    # Todo válido: agregamos al final de ambas listas manteniendo la sincronía.
                    herramientas.append(nombre_nuevo)
                    existencias.append(int(stock_nuevo))
                    print(f"\n✓ '{nombre_nuevo}' agregado con {stock_nuevo} unidades.")

    # Opción 7: Actualización de stock.

    elif opcion == "7":
        # Validación previa: no se puede operar si no hay herramientas cargadas.
        if len(herramientas) == 0:
            print("Error: no hay herramientas cargadas en el sistema.")

        else:
            nombre_buscado = input("Ingresá el nombre de la herramienta: ").strip()

            encontrado = False  # Bandera de búsqueda.

            for i in range(len(herramientas)):
                if herramientas[i].lower() == nombre_buscado.lower():
                    encontrado = True

                    print(f"\nHerramienta: {herramientas[i]}")
                    print(f"Stock actual: {existencias[i]} unidades.")
                    print("¿Qué operación querés realizar?")
                    print("  v - Venta (disminuir stock)")
                    print("  i - Ingreso (aumentar stock)")

                    operacion = input("Elegí una operación (v/i): ").strip().lower()

                    if operacion == "v":
                        cantidad_venta = input("Ingresá la cantidad a vender: ")

                        # Validamos que sea un número válido.
                        if not cantidad_venta.isdigit():
                            print("Error: ingresá un número entero positivo.")

                        else:
                            cantidad_venta = int(cantidad_venta)

                            # Validamos que haya stock suficiente para la venta.
                            if cantidad_venta > existencias[i]:
                                print(f"Error: stock insuficiente. Solo hay {existencias[i]} unidades disponibles.")
                            else:
                                existencias[i] -= cantidad_venta
                                print(f"\n✓ Venta registrada. Stock actualizado: {existencias[i]} unidades.")

                    elif operacion == "i":
                        cantidad_ingreso = input("Ingresá la cantidad a ingresar: ")

                        # Validamos que sea un número válido.
                        if not cantidad_ingreso.isdigit():
                            print("Error: ingresá un número entero positivo.")
                        else:
                            existencias[i] += int(cantidad_ingreso)
                            print(f"\n✓ Ingreso registrado. Stock actualizado: {existencias[i]} unidades.")

                    else:
                        print("Error: operación inválida. Elegí 'v' para venta o 'i' para ingreso.")

            # Si recorrimos toda la lista y no encontramos la herramienta, avisamos.
            if not encontrado:
                print(f"Error: '{nombre_buscado}' no existe en el catálogo.")

    # Opción 8: Salir.
    elif opcion == "8":
        print("Saliendo del sistema. ¡Hasta luego!")
        continuar = False

    # Opción Inválida.
    else:
        print("Opción inválida. Ingresá un número del 1 al 8.")