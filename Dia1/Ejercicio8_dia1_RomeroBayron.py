    ##################################
    #### Generar la serie del fibonacci########
    ##################################

print("##########################################")
print("Algoritmo que genera la serie del Fibonacci")
print("------------------------------------------")
num = int(input("Por favor ingrese la cantidad de digitos que quieres de la serie: "))
terminoUno = 0
terminoDos = 1
print(terminoUno)
print(terminoDos)

for i in range(2, num):
    terminoTres = terminoUno + terminoDos
    print(str(terminoTres))
    terminoUno = terminoDos
    terminoDos = terminoTres

# desarrollado por: Bayron Romero - C.C. 1005338700