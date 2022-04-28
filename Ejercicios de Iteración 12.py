def es_cuadrado_perfecto(limite):

    for x in range(limite,0,-1):
        if x**0.5 == int(x**0.5):
            print(str(x)+" es un numero entero")




limite = int(input("A partir de que numero quieres calcular los cuadrados perfectos?: "))

es_cuadrado_perfecto(limite)