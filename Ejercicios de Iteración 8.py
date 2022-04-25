cadena=input("Introduzca la cadena que desea utilizar: ")
separador=input("Cual es el separador dque desea utilizar?: ")

x2= cadena.split(separador)

print(x2)
x1=0

for x in range(len(cadena)):
    if cadena[x] == separador:
        #print("separador localizado en: "+ str(x))
        x1=x1+1
       

print("n.°                      Cadena")

for c1 in range(x1+1):
    if x2[c1]!='':
        print(str(c1+1) +"                      "+str(x2[c1]))



#myjoin2 = ' '.join(x2)
#print(myjoin2)

