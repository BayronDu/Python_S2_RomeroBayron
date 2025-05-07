####################################
###Custom Rappid Restaurat##########
####################################

print("El algoritomo le permite a la clientela personalizar el pedido de sus hamburguesas")
print("----------------------------------------------------------------------------------")
subTotal=0.0
total = 0.0
servicio = 0.0
cantHam = int(input("Digite la cantidad de hamburguesas que desea ordenar: "))
while cantHam <= 0:
    cantHam = int(input("!ERROR!\nPor favor digite una cantidad de hamburguesas valida: "))
    
print("INGREDIENTES A ELEGIR")
for i in range(0,cantHam):
    pan = int(input("Eleccion de pan: Digite 1 para pan de centeno (1000) o digite 2 para pan de avena(1500): "))
    while pan != 1 and pan !=2 :
        pan = int(input("¡ERROR! Por favor digite 1 para pan de centeno (1000) o digite 2 para pan de avena(1500): "))
    if (pan == 1):
        subTotal = subTotal + 1000
    else:
        subTotal = subTotal + 1500

    carne = int(input("Eleccion de carne: Digite 1 para 250g de carne (5000) o digite 2 para 300g de carne (7000)): "))
    while carne != 1 and carne !=2 :
        carne = int(input("¡ERROR! Por favor digite 1 para 250g de carne (5000) o digite 2 para 300g de carne (7000): "))
    if (carne == 1):
        subTotal = subTotal + 5000
    else:
        subTotal = subTotal + 7000

    pollo = int(input("Eleccion de pollo: Digite 1 para 250g de pollo (4500) o digite 2 para 350g de pollo (5500): "))
    while pollo != 1 and pollo !=2 :
        pollo = int(input("¡ERROR! Por favor digite 1 para 250g de pollo (4500) o digite 2 para 350g de pollo (5500): "))
    if (pollo == 1):
        subTotal = subTotal + 4500
    else:
        subTotal = subTotal + 5500

    polloD = int(input("Eleccion de pollo desmechado: Digite 1 para 250g de pollo desmechado (6500) o digite 2 para 350g de pollo desmechado (7500): "))
    while polloD != 1 and polloD !=2 :
        polloD = int(input("¡ERROR! Por favor digite 1 para 250g de pollo desmechado (6500) o digite 2 para 350g de pollo desmechado (7500): "))
    if (polloD == 1):
        subTotal = subTotal + 6500
    else:
        subTotal = subTotal + 7500

    tocineta = int(input("Eleccion de tocineta: Digite 1 para una lonja de tocineta (1500) o digite 2 para 2 lonjas de tocineta (2500): "))
    while tocineta != 1 and tocineta !=2 :
        tocineta = int(input("¡ERROR! Por favor digite 1 para una lonja de tocineta (1500) o digite 2 para 2 lonjas de tocineta (2500): "))
    if (tocineta == 1):
        subTotal = subTotal + 1500
    else:
        subTotal = subTotal + 2500

    papaF = int(input("Eleccion de papas fritas: Digite 1 para papas a la francesa (5000) o digite 2 para papas en cascos (6000): "))
    while papaF != 1 and papaF !=2 :
        papaF = int(input("¡ERROR! Por favor digite 1 para papas a la francesa (5000) o digite 2 para papas en cascos (6000): "))
    if (papaF == 1):
        subTotal = subTotal + 5000
    else:
        subTotal = subTotal + 6000

    bebida = int(input("Eleccion de bebidas: Digite 1 gaseosa (5000), digite 2 para Club Colombia (8000) o 3 para naranjada (9000): "))
    while bebida != 1 and bebida !=2 and bebida != 3:
        bebida = int(input("¡ERROR! Por favor digite 1 gaseosa (5000), digite 2 para Club Colombia (8000) o 3 para naranjada (9000): "))
    if (bebida == 1):
        subTotal = subTotal + 5000
    elif(bebida == 2):
        subTotal = subTotal + 8000
    else:subTotal = subTotal + 9000

servicio = subTotal * 0.10
total = subTotal + servicio
print("Cantidad de hamburguesas: ",cantHam)
print("Valor total: ", subTotal)
print("Valor total con servicio: ", total)


# desarrollado por: Bayron Romero - C.C. 1.005.338.700