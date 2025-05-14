contador = True
id =1 # Contador de personas
listaPersonas= [{"id":1005338700, "nombre": "bayron", "apellido": "romero", "edad": 27, "ciudadNacimiento": "b2ga","telefonoPersonal": 23,"telefonoTrabajo": 23},{"id":2, "nombre": "Yesica", "apellido": "Sanchez", "edad": 18, "ciudadNacimiento": "bga","telefonoPersonal": 432,"telefonoTrabajo": 2342}
,{"id":1, "nombre": "Camila", "apellido": "caceres", "edad": 14, "ciudadNacimiento": "bga","telefonoPersonal": 98,"telefonoTrabajo": 87}
]
while(contador):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    
    print("4. Actualizar a una persona en especifico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opcion (Numerica):"))
    
    if(opcionUsuario==1): 
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
       
        #ID,nombre, apellido, edad, ciudad de nacimiento, numero personal y numero de trabajo
        #contador de personas para nombrarlas en los inputs
        nombre=(input("Por favor, digite el nombre de la persona numero "+str(id)+ " :"))
        apellido=(input("Por favor, digite el apellidp de la persona numero" +str(id)+ ":"))
        edad=(int(input("Por favor, digite la edad de la persona numero " +str(id)+ " (en numero):")))
        ciudadNacimiento=(input("Por favor, digite la ciudad de nacimiento de la persona numero" +str(id)+ " :"))
        telefonoPersonal=(int(input("Por favor, digite el numero de telefono personal de la persona numero"+str(id)+ " :")))
        telefonoTrabajo=(int(input("Por favor, digite el numero de telefono de trabajo de la persona numero "+str(id)+ " :")))

        diccionarioPersona={"id":id, "nombre": nombre, "apellido": apellido, "edad": edad, "ciudadNacimiento": ciudadNacimiento,"telefonoPersonal": telefonoPersonal,"telefonoTrabajo": telefonoTrabajo}
        
        listaPersonas.append(diccionarioPersona)
        #print(listaPersonas)
        id = id+1 # Aumentamos el contador de personas
   
    elif (opcionUsuario == 2): #Opcion del menú
        if listaPersonas == []:
            print("---------------------------")
            print("#################")
            print("#### No hay personas ingresadas en el sistema. ####")
            print("#################")
        else:
            for i in range(len(listaPersonas)):
                print("#################")
                print("#### Persona #",i+1," ####")
                print("#################")
                print("ID:", listaPersonas[i]["id"])
                print("Nombre:",listaPersonas[i]["nombre"])
                print("Apellido:",listaPersonas[i]["apellido"])
                print("Edad",listaPersonas[i]["edad"])
                print("Ciudad Nacimiento",listaPersonas[i]["ciudadNacimiento"])
                print("Numero Personal",listaPersonas[i]["telefonoPersonal"])
                print("Numero Trabajo",listaPersonas[i]["telefonoTrabajo"])           
            
                print("---------------------------")           

    elif(opcionUsuario == 3):
        
        personaIndividual = (int(input("Por favor ingrese el ID (numérico) de la persona que desea consultar: ")))
        print("#################")
        print("#### Persona #"+str(personaIndividual+1)+" ####")
        id2 = personaIndividual-1
        print("#################")
        print("ID:", listaPersonas[id2]["id"])
        print("Nombre:",listaPersonas[id2]["nombre"])
        print("Apellido:",listaPersonas[id2]["apellido"])
        print("Edad",listaPersonas[id2]["edad"])
        print("Ciudad Nacimiento",listaPersonas[id2]["ciudadNacimiento"])
        print("Numero Personal",listaPersonas[id2]["telefonoPersonal"])
        print("Numero Trabajo",listaPersonas[id2]["telefonoTrabajo"])           
        print("---------------------------")   
    
    elif(opcionUsuario == 4):

        
        persMod = (int(input("Por favor ingresa el ID de la persona que deseas modificar: "))) ## id persona a modificar
        id3 = persMod - 1 #IDENTIFICADOR
        listaPersonas.pop(id3) #borra el diccionario en la posicion ide
        nombre=(input("Por favor, digite el nombre de la persona numero "+str(persMod)+ " :"))
        apellido=(input("Por favor, digite el apellidp de la persona numero" +str(persMod)+ ":"))
        edad=(int(input("Por favor, digite la edad de la persona numero " +str(persMod)+ " (en numero):")))
        ciudadNacimiento=(input("Por favor, digite la ciudad de nacimiento de la persona numero" +str(persMod)+ " :"))
        telefonoPersonal=(int(input("Por favor, digite el numero de telefono personal de la persona numero"+str(persMod)+ " :")))
        telefonoTrabajo=(int(input("Por favor, digite el numero de telefono de trabajo de la persona numero "+str(persMod)+ " :")))
    
        diccionarioPersona={"id":persMod, "nombre": nombre, "apellido": apellido, "edad": edad, "ciudadNacimiento": ciudadNacimiento,"telefonoPersonal": telefonoPersonal,"telefonoTrabajo": telefonoTrabajo}

        listaPersonas.insert(id3,diccionarioPersona)
       # print(listaPersonas)
    
    elif(opcionUsuario == 5):

        persEliminada = (int(input("Por favor digite el ID de la persona que desea eliminar de la lista: ")))
       # print(listaPersonas)

        for x in range(len(listaPersonas)):
            if(int(listaPersonas[x]["id"]) == persEliminada):
                listaPersonas.pop(x)
                break
                #print(listaPersonas[x]["nombre"])
                #print("valor de x: " +str(x))

    elif(opcionUsuario==6):
        print("Adios, vuelva pronto")
        contador=False
    else:
        print("No es una opción válida")
    