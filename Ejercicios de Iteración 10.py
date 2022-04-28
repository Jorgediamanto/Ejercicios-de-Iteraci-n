def imprimir_padres(nombres_padres,PERSONA):
    kau = 0
    for x in range(len(nombres_padres)):
        if ":"==nombres_padres[x]:
            variable_ayuda = nombres_padres.split(":")
            kau =1
            print("Un padre es "+ variable_ayuda[0])
            print("Y el otro es "+ variable_ayuda[1])


    if nombres_padres == "HUÉRFANO":
        print("Esta persona no tiene padres, es huérfano")

    if nombres_padres != "HUÉRFANO" and kau == 0:
        print("Esta persona solo tiene un padre, y es: "+nombres_padres)



def imprimir_hermanos(nombres_padres,PERSONA,v6):
    reiuwbg =0
    for x in range(len(PERSONA[0])):
        #print(nombres_padres+"  "+PERSONA[2][x])

        if nombres_padres == PERSONA[2][x] and v6-1!=x and PERSONA[2][x] !="HUÉRFANO":
            print(str(PERSONA[3][x])+" es un hermano de esta persona.")
            reiuwbg = 1

    if reiuwbg == 0:
        print("Esta persona no tiene hermanos.")






#nombre y apellido
IDENTIDAD = [["Raul","Paco","Eva","Santiago","Jaime"],["Gonzalez","Perez","Fernandez","Garcia","Martín"]]

#en el tipo persona: identificador, edad, padres, nombre
PERSONA = [[1,2,3,4,5],[24,14,2,96,27],["Paco Perez","HUÉRFANO","Paco Perez:Jaime Martín","Raul Gonzalez","Santiago Garcia:Paco Perez"],[IDENTIDAD[0][0]+" "+IDENTIDAD[1][0],IDENTIDAD[0][1]+" "+IDENTIDAD[1][1],IDENTIDAD[0][2]+" "+IDENTIDAD[1][2],IDENTIDAD[0][3]+" "+IDENTIDAD[1][3],IDENTIDAD[0][4]+" "+IDENTIDAD[1][4] ] ]



v1 = int(input("Desea dar una lista de todas las personas con una edad entre 20 y 30 años? (1 si 0 no): "))

if v1 == 1:
    print("Las personas con una edad entre 20 y 30 son: ")
    for x in range(len(PERSONA[0])):
        
        if PERSONA[1][x]<=30 and PERSONA[1][x]>=20:
            print(PERSONA[3][x])


v2 = int(input("Desea añadir un año a todas las personas de la lista? (1 si 0 no): "))

if v2 == 1:

    for x in range(len(PERSONA[0])):
        PERSONA[1][x] = PERSONA[1][x] +1

    print("Las nuevas edad con sus personas correspondientes son las siguientes: ")

    for x in range(len(PERSONA[0])):
        print(str(PERSONA[3][x])+" "+str(PERSONA[1][x])+ " años.")



v3 = int(input("Desea ver todos los huerfanos menores de 15 años? (1 si 0 no): "))

if v3==1:
    ratata =0
    for x in range(len(PERSONA[0])):
        
        if PERSONA[1][x]<15 and PERSONA[2][x]=="HUÉRFANO":
            print(PERSONA[3][x]+" es huérfano.")
            ratata = 1
    if ratata == 0:
        print("No hay huerfanos menores de 15 años.")

v4 = int(input("Desea conocer los padres de alguna persona? (1 si 0 no): "))

if v4 == 1:
    for x in range(len(PERSONA[0])):
        print(str(x+1)+"   "+PERSONA[3][x])

    v5 = int(input("Introduzca el numero corresponiendte a la persona que quiere saber sus padres: "))
 
    imprimir_padres(PERSONA[2][v5-1],PERSONA) 
 


v6 = int(input("Desea conocer los hermanos de alguna persona? (1 si 0 no): "))
if v6 == 1:
    for x in range(len(PERSONA[0])):
        print(str(x+1)+"   "+PERSONA[3][x])

    v6 = int(input("Introduzca el numero corresponiendte a la persona que quiere saber sus hermanos: "))
 
    imprimir_hermanos(PERSONA[2][v6-1],PERSONA,v6) 


