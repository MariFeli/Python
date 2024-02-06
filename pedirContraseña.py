contrasena_correcta = "contraseña123"

while True:
    contrasena_ingresada = input("Por favor ingresa tu contraseña: ")

    if contrasena_ingresada == contrasena_correcta:
        print("¡Contraseña correcta! Acceso concedido.")
        break  # Rompe el bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")
