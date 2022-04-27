def buscar_siguiente_palabra(c2):
    
    palabra2 = c2[1][0]
    x6 = 0
    for x in range(len(c2[1])):
        if c2[1][x]<palabra2:
            palabra2 = c2[1][x]
            x6 = x
            

    

    c2[0].remove(c2[0][x6])
    c2[1].remove(c2[1][x6])
    c2[2].remove(c2[2][x6])
    c2[3].remove(c2[3][x6])
            



    return palabra2, c2


def buscar_siguiente_palabra1(c1):
    
    palabra2 = c1[1][0]
    x66 = 0
    for x in range(len(c1[1])):
        if c1[1][x]>palabra2:
            palabra2 = c1[1][x]
            x66 = x
            

    

    c1[0].remove(c1[0][x66])
    c1[1].remove(c1[1][x66])
    c1[2].remove(c1[2][x66])
    c1[3].remove(c1[3][x66])
            



    return palabra2, c1

c1 = [[1,2,3,4],["avión","tren","auto","camión"],[3,4,'indice_min',1],[4,'...',1,2]]
c2 = [[1,2,3,4],["avión","tren","auto","camión"],[3,4,'indice_min',1],[4,'...',1,2]]
c3 = [[1,2,3,4],["avión","tren","auto","camión"],[0,0,0,0],[0,0,0,0]]

v111 = int(input("Desea eliminar una palabra? (1 si 0 no): "))

if v111 == 1:
    palabra_eliminar = input("que palabra desea eliminar: ")


    #YA ENTIENDO, NO FUNCIONABA POQREU AL BORRAR UN ELEMENTO Y ENTRAR A LOS SIGUIENTES COMO SE HABIA BORRADO UNO ENTRABA S EN UNO Q NO EXISTIA
        
    c="f"
    for y in range(len(c3[1])):
        
        if palabra_eliminar == c3[1][y]:
            c=y

    if c != 'f':
        c2[0].remove(c2[0][c])
        c2[1].remove(c2[1][c])
        c2[2].remove(c2[2][c])
        c2[3].remove(c2[3][c])

        c1[0].remove(c1[0][c])
        c1[1].remove(c1[1][c])
        c1[2].remove(c1[2][c])
        c1[3].remove(c1[3][c])


        c3[0].remove(c3[0][c])
        
        c33=c

        for zz in range(len(c3[0])-(c)):
            c3[0][c33] = c3[0][c33]-1
            c33 = c33 +1



        c3[1].remove(c3[1][c])
        c3[2].remove(c3[2][c])
        c3[3].remove(c3[3][c])

    if c== "f":
        print("No existe esa palabra en la lista.")




v112 = int(input("Desea añadir una palabra? (1 si 0 no): "))

if v112 == 1:
    palabra_añadir = input("que palabra desea añadir: ")

    for ramon in c3[0]:
        pablo = ramon

    c2[0].append(pablo+1)
    c2[1].append(palabra_añadir)
    c2[2].append(0)
    c2[3].append(0)

    c1[0].append(pablo+1)
    c1[1].append(palabra_añadir)
    c1[2].append(0)
    c1[3].append(0)


    c3[0].append(pablo+1)
    c3[1].append(palabra_añadir)
    c3[2].append(0)
    c3[3].append(0)


#CREAR ALGORITMO QUE CON CUALQUIER LISTA DE PALABRAS TE DE LA LISTA 'ANTERIOR' Y 'SIGUIENTE'

#PALABRA[1].sort()  NO SIRVE PRQ SOLO PUEDES CAMBIAR EL PALABRA[1] NO LOS OTROS

#este bucle busca la palabra mas pequeña

#ya he conseguido eliminar palabras y la tabla 'anterior'.  Me queda añadir palabras y la tabla 'siguiente'


palabra_min = c3[1][0]

x5 = 0

for x in range(len(c3[1])):
    if c3[1][x]<palabra_min:
        palabra_min = c3[1][x]
        x5 = x
        

#if x5 == 0:
 #   print("La nueva palabra min es: "+ palabra_min)

c2[0].remove(c2[0][x5])
c2[1].remove(c2[1][x5])
c2[2].remove(c2[2][x5])
c2[3].remove(c2[3][x5])


c3[2][x5] = "indice_min"

f5 = x5

n=0

palabra_escape = palabra_min

while n == 0:
    palabra_escape , c2 = buscar_siguiente_palabra(c2)
    
    


    #este bucle busca la posicion de la siguiente palabra
    for d1 in range(len(c3[1])):
        if c3[1][d1] == palabra_escape:
            x5=d1

    c3[2][x5] = c3[0][f5]

    f5 = x5

    if len(c2[1])==0:
        n=1
        


#hacer la tabla 'Siguiente' y ya solo me queda añadir elementos

palabra_max = c3[1][0]
x55 =0

for x in range(len(c3[1])):
    if c3[1][x]>palabra_max:
        palabra_max = c3[1][x]
        x55 = x
        


c1[0].remove(c1[0][x55])
c1[1].remove(c1[1][x55])
c1[2].remove(c1[2][x55])
c1[3].remove(c1[3][x55])

c3[3][x55] = "..."

f55 = x55

n1=0

palabra_escape1 = palabra_max

while n1 == 0:
    palabra_escape1 , c1 = buscar_siguiente_palabra1(c1)
    
    


    #este bucle busca la posicion de la siguiente palabra
    #creo que esto no esta bien asi que revisar ahora
    for d1 in range(len(c3[1])):
        if c3[1][d1] == palabra_escape1:
            x55=d1

    c3[3][x55] = c3[0][f55]

    f55 = x55

    if len(c1[1])==0:
        n1=1
        





letra = input("Introduzca la letra con la que quiere que empiezen sus palabras: ")

print("Palabras que empiezan por la letra "+str(letra)+": ")

cxx = 0

for x in c3[1]:
    if x[0] == letra:
        print(x)
        cxx=1

if cxx == 0:
    print("No se encuentran palabras que cumplan las condidciones requeridas.")

print("Lista final ordenada: ")
print(c3)   
