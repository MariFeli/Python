#Un programador de videojuegos, quiere qué el usuario adivine un número para
#mostrar como prototipo de videojuegos creado en Python

print("***BIENVENIDO A ESTA PEQUEÑA ADIVINANZA**")
numero_adivinar = 9 #El número que él usuario debe ingresar
print("El número a adivinar se encuentra en un rango de 1 a 10 ") #Hemos decidido dar un rango para ayudar al usuario.
NumeroIngresar= int(input ("Introducir el número a adivinar: ")) #Pedimos un número
adivinar = False 
while adivinar == False : #Iniciamos el bucle
    if NumeroIngresar == numero_adivinar: #Si el número ingresado es igual al de adivinar
        adivinar= True  #La condición es verdadera      
        print("**Felicidades, es el número correcto**") #Imprimimos el siguiente mensaje
        break #Detenemos el bucle
    else:
        print("No es el número, intenta una vez más") 
    NumeroIngresar= int(input ("Introducir el número a adivinar: ")) #De lo contrario solicitamos de nuevo un número
print("Juego Finalizado")  #Imprimimos mensaje. 
