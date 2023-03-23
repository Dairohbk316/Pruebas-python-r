import random

num = int(input('digite el numero de referencia >>> '))
comparador = random.randint(0,1000)
contador = 0
lista = []
print(comparador)

while  comparador <= num:
    print(comparador)
    contador += 1
    lista.append(contador)
    print(lista)