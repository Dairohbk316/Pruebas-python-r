lista = []

for i in range(0, 100):
    if i % 2 == 1:
        lista.append(i)

print(lista) 

list_comprehesion = [i for i in range(0, 100) if i % 2 ==0]
print(list_comprehesion)