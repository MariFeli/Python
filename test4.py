# x = 9.65
# y=x
# #y = 1.32
# print(id(x))
# print(id(y))

# x = 10
# print(id(x))
# y= 10
# print(id(y))

# x = ["hola", 4, 5]
# print(isinstance(x,int))

# # print(type(x))
# # print(id(x))
# # x[0]= "Agur"
# # print(id(x))

# x = input("Introducir una cifra")
# if isinstance (x,int):
#     x*2
# else:
#     print("No es lo esperado")

#Confirmar que la variable inflación es un tipo float e inmutable.
    
# inflacion = 5.7654
# print(id(inflacion))
# print(type(inflacion))
# print(isinstance(inflacion,int))

 #imprimir la suma de todos que son del tipo int (número entero). La respuesta en este caso es 15.

# x = [5 , 4.32 , 10]
# suma=0
# for i in x:
#     if isinstance (i,int):
#         suma += i


# print(suma)

# i = 0
# while i<10:
#     print("Hola" + str(i))
#     i=i+1
# print("End")


# i = 1
# while i < 10:
#     print (i)
#     i += 1

#Imprimir los valores desde 50 hasta 100
# x = 50
# while x < 100:
#     print(x)
#     x += 1

#Desde 5, imprimir los valores 5 a 20, pero excluye 12.

numero = 5
while numero < 21:
    if numero != 12:
        print(numero)
    numero += 1
#Un usuario de página web desea introducir las edades de los usuarios entre 18 y 65
#las veces que sean necesarias para que no se metan datos incorrectos

EdadUsuario = 18
edad= int (input("¿Cuál es su edad? "))
while edad >= 65 :
    if edad >= EdadUsuario:
        print("Su edad ha sido guardada con éxito")
        break
    else:
        print("Por Favor introduce la edad correcta")
        edad= int (input("¿Cuál es su edad? "))   
print("End")



    



    

    




        










