def maximo_comun_divisor(numero1,numero2):
    r=1
    if numero1 % numero2 == 0:
        return numero2

    while True:
        f=numero1
        numero1 = numero2
        numero2 = f%numero2
        
        
        if numero2!=0:
            r=numero2

        if numero2 ==0:
            break
        
    
    return r














x=0

numero1 = int(input("Introduzca el primer valor con el que desea calcular el maximo comun divisor: "))


numero2 = int(input("Introduzca el segundo valor con el que desea calcular el maximo comun divisor: "))

if numero1 < numero2:
    x = numero1
    numero1 = numero2
    numero2 = x

raa = maximo_comun_divisor(numero1,numero2)

print("Maximo común divisor entre los dos números es: "+str(raa))