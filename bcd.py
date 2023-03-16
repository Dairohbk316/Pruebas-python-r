numero_decimal = int(input("Numero decimal a convertir -->> "))
modulos = []

while numero_decimal != 0:
    modulo = numero_decimal % 2
    residuo = numero_decimal // 2
    
    modulos.append(modulo)
    numero_decimal = residuo

modulos.reverse()    

print(modulos)   