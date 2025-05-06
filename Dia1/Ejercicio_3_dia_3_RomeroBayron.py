##################################
#### Factorial de un numero ######
##################################

print("##########################################")
print("Algoritmo muestra el factorial de un numero")
print("------------------------------------------")

fact = 1
num = int(input("Ingrese el numero: "))

for i in range (num,1,-1):

    fact = fact * i

print("El numero factorial de: "+str(num)+ " es: "+str(fact))

# desarrollado por: Bayron Romero - C.C. 1005338700