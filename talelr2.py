
palabra=input("digite la palabra:  ")

def inversa (cadena):
    cadena=list(cadena)
    cadena.reverse()
    return "".join(cadena)

print(inversa(palabra))

def comparar(cadena):
    return cadena == inversa(cadena)

print(comparar(palabra))

numeros=list(input("Digite los números:   ")) 

def histograma(num):
    
    p=list(num)
    
    numeros=len(p)
    
    for cant in range(numeros):
        asterisco=int(p[cant])
        print("*"*asterisco)

histograma (numeros)