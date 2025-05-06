    ##################################
    ####Programa para verificar si un numero es o no primo##########
    ##################################

from re import match

print("##########################################")
print("Algoritomo que indica si el numero ingresado es primo")
print("------------------------------------------")
num = int(input("Por favor digite el numero que desea verificar: "))
temp = 0
for i in range(1, num):
    conteo = num / i
   
    if (conteo) % 2 == 0:
        temp = temp+1

if temp < 2:
    print("El numero "+str(num)+" es primo")
else:
    print("El numero "+str(num)+ " no es primo")


# desarrollado por: Bayron Romero - C.C. 1005338700