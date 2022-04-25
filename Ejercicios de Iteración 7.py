from unittest import result


def cambiar_base(numero_entero,base):
    conversion_cadena="0123456789ABCDEF"
    if numero_entero<base:
        return conversion_cadena[numero_entero]
    
    else:
        return cambiar_base(numero_entero//base, base) + conversion_cadena[numero_entero % base]


numero_entero = int(input("Que numero desea cambiar de base?: "))
base = int(input("A que base desea cambiar el numero: (2<=n)"))

resultado = cambiar_base(numero_entero,base)

print(resultado)