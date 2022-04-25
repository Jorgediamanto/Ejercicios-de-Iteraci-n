
from dataclasses import dataclass

@dataclass
class Cuenta:
    nombre: str
    dinero: float
    dinero_mes_pasado: float
    dinero_retirado: float
    dinero_ingresado: float
    numero_cuenta: int
    numero_transacciones: int
    


cuenta1 = Cuenta(input("introduzca nombre propietario: "), float(input("Introduzca cantidad de dinero en la cuenta: ")),float(input("Introduzca cantidad de dinero en la cuenta el mes pasado: ")),0,0,input("Introducir numero de cuenta: "),0)

n=1
while n==1:


    v1 = input("Desea retirar dinero de la cuenta? (1 si  0 no): ")

    if v1 == "1":
        cuenta1.dinero_retirado = float(input("Cuanto dinero desea retirar: "))
        cuenta1.numero_transacciones = cuenta1.numero_transacciones +1

    v2 = input("Desea ingresar dinero de la cuenta? (1 si  0 no): ")
    if v2 == "1" :
        cuenta1.dinero_ingresado = float(input("Cuanto dinero desea ingresar: "))
        cuenta1.numero_transacciones = cuenta1.numero_transacciones +1





    

    dia = input("Que dia del mes es?: ")
    if dia == "1":
        cuenta1.numero_transacciones =0
        cuenta1.dinero_mes_pasado = cuenta1.dinero

    cuenta1.dinero = cuenta1.dinero -cuenta1.dinero_retirado + cuenta1.dinero_ingresado
    cuenta1.dinero_ingresado=0
    cuenta1.dinero_retirado=0

    beneficios=float(input("Introduzca un valor y le diremos si sus beneficios respecto al mes anterior es mayor: "))

    if beneficios>(cuenta1.dinero-cuenta1.dinero_mes_pasado):
        print("Sus beneficios no son lo suficientemente altos")

    else:
        print("Sus beneficios son mayores a la cifra dada")

    print("El saldo de esta cuenta es de "+str(cuenta1.dinero)+" y el numero de transacciones es de "+str(cuenta1.numero_transacciones))



    n=float(input("Desea continuar haciendo operaciones? 1 si  0 no: "))



