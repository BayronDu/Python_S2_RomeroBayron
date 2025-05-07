#########################
###### Clase Dia 1 ######
#########################



# Imprimir en python
print("Hola Mundo!")

# creacion de variables
#1. Dato tipo string
nombre = "Pedro"

print(type(nombre))
#dato tipo numero entero
numeroEntero = 5
print(numeroEntero)
print(type(numeroEntero))
#3. dato tipo numero real
numeroReal = 5.3
print(type(numeroReal))
#convertir numero int a float
numeroNuevo = float(numeroEntero)
print(numeroNuevo)


#cliclo for
for i in range (5):
    print(i)
    print("")

#ciclo for (Hasta)
for i in range(0,5):
    print(i)
    print("")

#cliclo for (desde - hasta)
for i in range(1,5):
    print(i)
    print("")

#ciclo for (desde-hasta-paso)
for i in range (1,5,1):
    print(i)
    print(" ")

# ciclo While
booleanitoNuevo = True
while(booleanitoNuevo == True):
    print ("Sigo siendo verdadero")
    booleanitoNuevo = False

while(booleanitoNuevo):
    print("sigo siendo verdadero")
    booleanitoNuevo = False


# condicionales if-else
texto = "Corpus"
if(texto == "Corpus"):
    print ("Sos Corpus")
elif(texto == "Sharick"):
    print("Sos Sharick")
else:
    print("No sos ninguno")

# anidar condicionales

booleanitoCorpus1= True
booleanitoCorpus2= False

if(booleanitoCorpus1 == True):
    print("Todos somos verdaderos")
else:
    print("No somos iguales")

#####################
# Entradas de usuario
nombreUsuario = input("Cual es tu nombre?")
print("tu nombre es: "+nombreUsuario)#concatenacion
edadUsuario = input ("Cual es tu edad?")
print("Tu nombre es: "+nombreUsuario+" y tu edad es: "+edadUsuario)

####################################
#funcion con retorno y con parametros
def areaCirculo(radio):
    valorPi = 3.1416
    resultadoFinal = valorPi * (radio**2)
    return resultadoFinal
radioUsuario = float(input("cual es el radio de su circulo?"))
print("el area del circulo es: "+str(int(areaCirculo(radioUsuario))))

#funcion con retorno y sin parametros

def valorDolar():
    return 4299
valorFinalDolar = valorDolar()
print("el valor del dolar es: "+str(valorFinalDolar))

#



# desarrollado por: Bayron Romero - C.C. 1005338700