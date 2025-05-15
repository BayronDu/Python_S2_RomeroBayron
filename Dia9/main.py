#Programa de gestion de datos de artistas musicales

from funcion.funcionesGGDD import *

booleanito = True
#listaArtistas=abrirJSON()

while(booleanito):
    listaArtistas = abrirJSON()
    print("#################")
    print("#### Lista de artistas ####")
    print("#################")

    print("1. Resgistrar artista")
    print("2. Generar un informe")
    print("3. Módulo de Reportes:")
    opcionUsuario = int(input("Escoja una opción numérica: "))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear artista ####")
        print("#################")
        # Obtener datos del nuevo usuario
        nombreArtista = input("Por favor, ingrese el nombre del artista: ")
        paisArtista = input("Por favor, ingrese el pais de origen artista: ")
        aniosArtista = int(input("Años activo (Periodo)"))
        primerDiscoArtista = int(input("Por favor, ingrese el año del primer lanzamiento: "))
        generoMusical = input("Por favor, el genero musical: ")
        unidadesTotales = float(input("Por favor, ingrese las unidades certificadas totales: "))
        ventasReclamadas = float(input("Por favor, ingrese las ventas reclamadas: "))
        estadoArtista = input("¿El artista se encuentra activo? ")
        

