print('')
print('Bult-In Functions')
print('')
print('1: Pow')
print('2: Filter')
print('3: getattr')
print('4: staticmethod')
print('5: range')

opccion=input('Que funcion quiere ver: ')
opccion=int(opccion)

#################### Opccion #1

if opccion==1:
    print ('____________________________')
    print ('Built-in Functions (pow): ')
    print ('saca la potencia de un numero')
    print (' ')
    base = input('Digite el numero base:  ')
    base= int(base)
    exponente = input('Digite el exponente:  ')
    exponente=int(exponente)

    fpow= pow(base,exponente)

    print ('FUNCION POW: ', fpow)
    print ('____________________________')

#################### Opccion #2

if opccion==2:
    print ('____________________________')
    print ('Built-in Functions (filter)')
    print ('es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición.')
    print (' ')	
    def numerospares():
        numeros=[5, 12, 17, 18, 24, 32]
        pares=[]
        for numero in numeros:
            par = numero%2
            if par  == 0:
                pares.append(numero)

        print(pares)

    numerospares()
    print ('____________________________')

################### Opccion #3

if opccion==3:
    print ('____________________________')
    print ('Built-in Functions (Getattr)')
    print ('permite obtener el valor de un atributo indicando su nombre como una cadena.')
    print ('')
    class TipoAnimales:
        nombre = "Tigre"
        clase = "Salvaje"
        habitad = "Selva"

    animal1=getattr(TipoAnimales,'nombre')
    animal=getattr(TipoAnimales,'reproduccion','no existe ese atributo')
    print(animal1)
    print(animal)
    print ('____________________________')

if opccion==4:
	

    