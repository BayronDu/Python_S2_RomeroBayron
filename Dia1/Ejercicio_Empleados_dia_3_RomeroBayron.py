##################################
#### Factorial de un numero ######
##################################

print("##########################################")
print("Algoritmo que calcula el salario de una cantidad de empleados determinada")
print("------------------------------------------")
netoMayor = 0.0
netoMenor = salarioBrutoTotal = salarioNetoTotal = netoMayor= epsTotal = pensionTotal = 0.0
valorHora = 20000
nomMayor = ""
nomMenor = "" 


cantEmp = int(input("Bienvenido a ACME. Por favor digite la cantidad de empleados a los que se quiere calcular el salario: "))
while cantEmp <= 0:
    cantEmp = int(input(("ERROR. Por favor digite un numero valido: ")))

for i in range(0,cantEmp):
    nomEmp = str(input("Por favor digite el nombre del empleado: "))
    cantHoras = int(input("Por favor digite la cantidad de horas trabajadas: "))

    salarioBruto = valorHora * cantHoras
    pension = salarioBruto * 0.04
    eps = salarioBruto * 0.04
    salarioNeto = salarioBruto - eps - pension

    if salarioNeto < netoMenor or netoMenor == 0:
        netoMenor = salarioNeto
        nomMenor = nomEmp
    if salarioNeto > netoMayor:
        netoMayor = salarioNeto
        nomMayor = nomEmp

        salarioBrutoTotal = salarioBrutoTotal + salarioBruto
        epsTotal = epsTotal + eps
        pensionTotal = pensionTotal + pension
        salarioNetoTotal = salarioNetoTotal + salarioNeto

print("Estadistica totales: ")
print("Total de salarios brutos: ", salarioBrutoTotal)
print("Total de pagos a pension: ", pensionTotal)
print("Total de pagos a EPS: ",epsTotal)
print("###############################################################")
print("El empleado que mas dinero generó fue: ",nomMayor, " con un salario neto de: ",netoMayor)
print("El empleado que menos dinero generó fue: ",nomMenor, " con un salario neto de: ",netoMenor)




# desarrollado por: Bayron Romero - C.C. 1005338700