#Un programador de videojuegos, quiere qué el usuario adivine un número para
#mostrar como prototipo de videojuegos creado en Python

numero_adivinar = 9
print("El número a adivinar se encuentra en un rango de 1 a 10 ")
NumeroIngresar= int(input ("Introducir el número a adivinar: "))
adivinar = False
while adivinar == False :
    if NumeroIngresar == numero_adivinar:        
        print("Felicidades, es el número correcto") 
        break
    else:
        print("No es el número, intenta una vez más")
    NumeroIngresar= int(input ("Introducir el número a adivinar: "))
print("Juego Finalizado")  
