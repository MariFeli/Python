#Preguntar al usuario por números hasta que el usuario 
#introduzca “q” para quit. Sumar los valores y imprimir el resultado final.
    
def sumarNumeros():
    suma = 0
    while True: #cuando necesitas crear un bucle infinito hasta que necesitas una razón para salir.
        numero = input("Por favor ingresa un número o 'q' para salir: ")
        if numero.lower() == 'q': #lower método de las cadenas que permite convertir los caracteres a minúscula.
            break #Terminamos el bucle infinito
        try:
            suma += float(numero)
        except ValueError: #Manejar cualquier error que pueda ocurrir durante la conversión del némero ingresado
            print("Por favor ingresa un número válido o 'q' para salir.")
    return suma

resultado = sumarNumeros()
print("La suma de los números ingresados es:", resultado)


