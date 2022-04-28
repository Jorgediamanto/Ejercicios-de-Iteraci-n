def maximo_comun_divisor(numero1,numero2):
    
    
    r=1

    if numero1 % numero2 == 0:
        return numero2



    for x in range(int(numero2/2),0,-1):
        if numero1 % x == 0 and numero2 % x == 0:
            r = x
            break

    return r

x =0

numero1 = int(input("Introduzca el primer valor con el que desea calcular el maximo comun divisor: "))


numero2 = int(input("Introduzca el segundo valor con el que desea calcular el maximo comun divisor: "))

if numero1 < numero2:
    x = numero1
    numero1 = numero2
    numero2 = x
    

raa = maximo_comun_divisor(numero1,numero2)

print("Maximo común divisor entre los dos números es: "+str(raa))

