letra = input("Introduzca la letra con la que quiere que empiezen sus palabras: ")

diccionario = ["avión","tren","auto","camión"]

c1=0
print("Palabras que empiezan por la letra "+str(letra)+": ")
for x in diccionario:
    if x[0] == letra:
        print(x)
        c1=1

if c1 == 0:
    print("No se encuentran palabras que cumplan las condidciones requeridas.")