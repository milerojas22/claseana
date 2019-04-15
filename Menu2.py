import math 
from random import randint, uniform, random

print('')
print('Numerical and Mathematical Modules')
print('')
print('1: Sqrt')
print('2: Random')
print('3: isclose')

opccion=input('Que funcion quiere ver: ')
opccion=int(opccion)

if opccion==1:
    print ('____________________________')
    print (' ')
    print ('Devuelve la raíz cuadrada de un numero .')
    print (' ')

    numero = input('Digite el numero de la raiz cuadrada ')
    numero= int(numero)
    
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
