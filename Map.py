# Funcion Map ejecuta funcion para cadal elemento iterable
# El elemtno se envia a la funcion como parametro

#map(fucion, iterables)

numbers = [1,2,3,4,5,6,78,9,0]

numbers_v2 = []

for i in numbers:
    numbers_v2.append(i ** 2)

print(numbers_v2)    


trasnformacion = list(map(lambda i: i * 2, numbers_v2))  #utilizo la lambda para tomari i y ese i x 2, de la lista numbers_v2

#Hacemos una transformacion de la funcion original 

def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

numeros_v2 = list(map(doblar, numeros))
lambda_numeros = list(map(lambda i : i // 2, numbers_v2))
print(numeros_v2)
print(lambda_numeros)


sumatoria = list(map(lambda i: i + 1, numeros))
print(sumatoria)


print(sum(sumatoria))


def longitud_palabras(frase): # Función
    palabra_len = list(map(len, frase.split())) # Longitud de cada palabra
    return print(palabra_len )# Retornar resultado

longitud_palabras('Hola Luis, como estas?')

frase_V2 = ('Sintaxis y funciones de Python split Si no se especifica un parametro concreto, Python split divide la cadena correspondiente en cada espacio. El parametro separator marca la cadena de caracteres que se debe separar. Cada vez que se cumple esta condicion o marca, se efectua el correspondiente fraccionamiento')

contador_letras = list(map(len, frase_V2.split() ))
print(f'Contador de letras, {contador_letras}')
print(sum(contador_letras))

resultado = list(map(lambda x, y: x + y, numbers, numeros))




