    ##################################
    #### calcular el promedio de una lista de numeros##########
    ##################################

print("##########################################")
print("Algoritmo que calcula el promedio de una serie de numeros")
print("------------------------------------------")
suma = 0.0
promedio = 0.0
cantNum = int(input("Digite la cantidad de numeros a promediar: "))
for i in range(0, cantNum):
    num = float(input("Ingrese el número: "))
    suma = suma + num
promedio = suma / cantNum
print("El promedio es: "+ str(promedio))

# desarrollado por: Bayron Romero - C.C. 100533870