"""
Diseño Digital Moderno grupo: 4
Semestre 2024-2
Equipo 9
Integrantes del equipo:
Cruz Maldonado Armando
Leon Flores Pedro David
Pozos Hernandez Angel
Mora Ortega Judith
"""

def validar_numero(numero, base):
    try:
        int(numero, base) # intentar convertir el número a decimal
        return True # si no hay error, el número es válido
    except ValueError:
        try:
            float(numero)
            return True
        except ValueError:
            if base == 16:
                if all(digito.isdigit() or digito.upper() in 'ABCDEF' for digito in numero.split('.')[1]):
                    return True
                else:
                    return False
            else:
                return False # si hay error, el número no es válido

def separar_partes(numero):
    partes = numero.split(".") # dividir el número por el punto decimal
    if len(partes) == 1: # si solo hay una parte, es la parte entera
        parte_entera = partes[0]
        parte_decimal = "0" # la parte decimal es cero
    elif len(partes) == 2: # si hay dos partes, son la parte entera y la decimal
        parte_entera = partes[0]
        parte_decimal = partes[1]
    else: # si hay más de dos partes, el número no es válido
        parte_entera = "0"
        parte_decimal = "0"
    return parte_entera, parte_decimal # devolver una tupla con las dos partes

def convertir_parte_entera_a_decimal(parte_entera, base):
    return int(parte_entera, base) # convertir la parte entera a decimal

def convertir_parte_decimal_a_decimal(parte_decimal, base):
    resultado = 0 # inicializar el resultado
    for i, digito in enumerate(parte_decimal): # recorrer cada dígito de la parte decimal
        digito_decimal = int(digito, base) # convertir el dígito a decimal
        exponente = -(i + 1) # calcular el exponente negativo
        resultado += digito_decimal * (base ** exponente) # sumar el producto al resultado
    return resultado # devolver el resultado

def convertir_decimal_a_otra_base(decimal, base):
    residuos = [] # inicializar la lista de residuos
    while decimal > 0: # mientras el número sea mayor que cero
        residuo = decimal % base # calcular el residuo de la división
        residuo_hex = hex(residuo)[2:] # convertir el residuo a hexadecimal si es necesario
        residuos.append(residuo_hex) # agregar el residuo a la lista
        decimal = decimal // base # actualizar el número con el cociente de la división
    residuos.reverse() # invertir la lista de residuos
    resultado = "".join(residuos) # convertir la lista a una cadena
    return resultado # devolver el resultado

def convertir_decimal_con_punto_a_otra_base(decimal, base):
    parte_entera = int(decimal) # obtener la parte entera del número
    parte_decimal = decimal - parte_entera # obtener la parte decimal del número
    parte_entera_otra_base = convertir_decimal_a_otra_base(parte_entera, base) # convertir la parte entera a otra base
    parte_decimal_otra_base = [] # inicializar la lista de la parte decimal en otra base
    for _ in range(4): # iterar cuatro veces
        parte_decimal *= base # multiplicar la parte decimal por la base
        parte_entera_decimal = int(parte_decimal) # obtener la parte entera del resultado
        parte_entera_decimal_hex = hex(parte_entera_decimal)[2:] # convertir la parte entera a hexadecimal si es necesario
        parte_decimal_otra_base.append(parte_entera_decimal_hex) # agregar la parte entera a la lista
        parte_decimal -= parte_entera_decimal # actualizar la parte decimal con la diferencia
    parte_decimal_otra_base = "".join(parte_decimal_otra_base) # convertir la lista a una cadena
    resultado = f"{parte_entera_otra_base}.{parte_decimal_otra_base}" # formatear el resultado con un punto decimal
    return resultado # devolver el resultado

while True: # repetir hasta que el usuario quiera salir
    print("\nSelecciona la base del numero que quieras convertir:")
    print("1. Base 2 - Binario")
    print("2. Base 8 - Octal")
    print("3. Base 10 - Decimal")
    print("4. Base 16 -Hexadecimal")
    print("5. Salir")

    opcionb = input("Selecciona una opción (1-5): ")

    if opcionb == '1':
        base_origen = 2 # la base del número es 2
    elif opcionb == '2':
        base_origen = 8 # la base del número es 8
    elif opcionb == '3':
        base_origen = 10 # la base del número es 10
    elif opcionb == '4':
        base_origen = 16 # la base del número es 16
    elif opcionb == '5':
        print("Saliendo del programa.")
        break # salir del bucle
    else:
        print("Opción no válida. Ingresa un número del 1 al 5.")
        continue # volver al inicio del bucle

    while True: # repetir hasta que el usuario elija una base válida
        print("\nAhora, selecciona la base a la que quieras convertir el número:")
        print("1. Base 2 - Binario")
        print("2. Base 8 - Octal")
        print("3. Base 10 - Decimal")
        print("4. Base 16 - Hexadecimal")

        opcionc = input("Selecciona una opción (1-4): ")

        if opcionc == '1':
            base_destino = 2 # la base destino es 2
            break # salir del bucle
        elif opcionc == '2':
            base_destino = 8 # la base destino es 8
            break # salir del bucle
        elif opcionc == '3':
            base_destino = 10 # la base destino es 10
            break # salir del bucle
        elif opcionc == '4':
            base_destino = 16 # la base destino es 16
            break # salir del bucle
        else:
            print("Opción no válida. Ingresa un número del 1 al 4.")

    while True: # repetir hasta que el usuario ingrese un número válido
        numero = input(f"Ingresa un número en base {base_origen}, el cual deseas convertir a base {base_destino}: ")
        if validar_numero(numero, base_origen): # si el número es válido
            break # salir del bucle
        else: # si el número no es válido
            print(f"Número no válido. Ingresa un número en base {base_origen}.")

    parte_entera, parte_decimal = separar_partes(numero)

    # Conversión de la parte entera a decimal
    parte_entera_decimal = convertir_parte_entera_a_decimal(parte_entera, base_origen)

    # Conversión de la parte decimal a decimal
    parte_decimal_decimal = convertir_parte_decimal_a_decimal(parte_decimal, base_origen)

    # Convertir la parte entera y la parte decimal a la base de destino
    resultado_parte_entera = convertir_decimal_a_otra_base(parte_entera_decimal, base_destino)
    resultado_parte_decimal = convertir_decimal_con_punto_a_otra_base(parte_decimal_decimal, base_destino)

    print(f"\nEl número {numero} en base {base_origen} es {resultado_parte_entera}{resultado_parte_decimal} en base {base_destino}.")