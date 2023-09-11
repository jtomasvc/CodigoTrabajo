# Arreglo donde se almacenaran los numeros
numeros = []

# Le agregamos 3 números
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# Asumir que el menor es el primero de la lista
menor = numeros[0]
# Recorre el arreglo y compara los numeros ingresados
for numero in numeros:
    if numero < menor:
        menor = numero
# Imprimir el resultado
print("Menor:", menor)