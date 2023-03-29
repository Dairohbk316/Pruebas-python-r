# La funcion Filter crea un nuevo iterador
# filter (funcion, iterable)

lista = [1, 2 ,3, 4 ,5, 778887, 565, 457, 48, 60, 42]

numeros = list(filter(lambda x: x % 2 == 0, lista ))

print(numeros)