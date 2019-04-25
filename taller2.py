palabra=input("digite la palabra:  ")

def inversa (cadena):
    cadena=list(cadena)
    cadena.reverse()
    return "".join(cadena)

print(inversa(palabra))

def comparar(cadena):
    return cadena == inversa(cadena)


def histograma():