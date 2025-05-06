    ##################################
    #### Tabla de multiplicar ########
    ##################################

print("##########################################")
print("Algoritmo que genera la tabla de multiplicar del numero que se ingrese")
print("------------------------------------------")
num = int(input("Por favor ingrese el numero de la tabla que deseas visualizar: "))

for i in range(1,10,1):
    multi = num * i
    print(str(num) + " * "+ str(i)+ " = " + str(multi))

# desarrollado por: Bayron Romero - C.C. 1005338700