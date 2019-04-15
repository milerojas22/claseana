print ('Bibliotecas Python3')
print ('1. Bult-In Function')
print ('2. Numerical and Mathematical Modules')

opccion1 = input('Que ejercicio quiere ver: ')
opccion1 = int(opccion1)

while opccion1 <3:

    if opccion1==1:
        print('Bult-In Functions')
        print('')
        print('1: Pow')
        print('2: Filter')
        print('3: Getattr')
        print('4: Zip')
        print('5: Iter')

        opccion=input('Que funcion quiere ver: ')
        opccion=int(opccion)

        while opccion<6:
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
                print ('____________________________')
                print ('Built-in Functions (Zip)')
                print ('toma como argumento dos o más objetos iterables (idealmente cada uno de ellos con la misma cantidad de elementos)')
                print ('')
                ropas = ["Pantalon", "Blusa", "Chaqueta", "Cantidad"]
                cantidades = [14, 14, 27, 24]
                list(zip(ropas, cantidades))   
                for ropa, cantidad in zip(ropas, cantidades):
                    print ("cantidad en el almacen de {}: {} ".format(ropa, cantidad))

            if opccion==5:
                print ('____________________________')
                print ('Built-in Functions (Iter)')
                print ('crea un objeto que puede ser iterado un elemento a la vez.')
                print ('')

                lista = [10, 100, 1000, 10000]
                iterador = iter(lista)
                comida = iter(["perro caliente", "hamburguesa", "salchipapa"])
                print(next(comida))
                print(next(comida))
                print(next(comida))

            if opccion1 >=6:
                print ('la opcion no es valida ')

    if opccion1==2:

        print('')
        print('Numerical and Mathematical Modules')
        print('')
        print('1: Sqrt')
        print('2: Random')
        print('3: isclose')

        opccion=int (input('Que funcion quiere ver: '))

        while opccion<=3:

            if opccion==1:
                print ('____________________________')
                print (' ')
                print ('Devuelve la raíz cuadrada de un numero .')
                print (' ')

                numero = int (input('Digite el numero de la raiz cuadrada '))
    
    
                print (math.sqrt (numero))

            if opccion==2:
                print ('____________________________')
                print (' ')
                print ('Randint: Esta función recibe dos números entre los cuales queremos que se genere un número aleatorio entero.')
                print (' ')
                print (randint(0,16))
                print ('Uniform: Genera un número aleatorio decimal.')
                print (' ')
                print (uniform(0,16))
                print ('Random: Esta es la función base para la generación de números aleatorios. ')
                print (' ')
                print (random())

            if opccion==3:
                print ('____________________________')
                print (' ')
                print ('Devuelva True si los valores a y b están cerca uno del otro y de lo False contrario.')
                print (' ')
                numero1 = int (input('Digite el primer numero: '))
                numero2 = int (input('Digite el segundo numero: '))

                print (math.isclose(numero1, numero2))

            if opccion1 >=4:
                print ('la opcion no es valida ')

if opccion1 >=6:
	print ('la opcion no es valida ')
