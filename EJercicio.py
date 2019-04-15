# numero1 = input ("Digite el numero 1 : ")
# numero1 = int(numero1)

# numero2= input ("Digite el numero 2 : ")
# numero2 = int(numero2) 


# def numeromayor (numero1, numero2):

#     if numero1 > numero2:
            
#         print ("el numero mayor es : ", numero1)

#     elif numero1 < numero2:

#         print ("el numero mayo es: ", numero2)

#     else:

#         print ("los numeros son iguales")


# # print(numeromayor(numero1, numero2))


# lista = ['a','e','i','o','u']

# def cantidad (lista):

#     cont=0


#     for x in lista:
#         print (x)
#         cont = cont + 1
#         print (cont)
#         # x = x + 1

#     return cont

# print (cantidad(lista))


lista1 = [1,2,3]
lista2 = [3,5,1]

def compara (lista1, lista2):

    for x in lista1:
        for y in lista2:
            if x == y:
                print("el numero esta igual", x)
                break

print(compara(lista1, lista2))







    	

    	
