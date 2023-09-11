def fibonacci(n):
  # Definir los primeros dos números de la serie
  num1 = 1
  num2 = 10

  # Crear un arreglo para almacenar los números de la serie
  fib = [num1, num2]

  # Generar los números restantes y almacenar en la lista
  for i in range(2, n):
    num3 = num1 + num2
    fib.append(num3)
    num1 = num2
    num2 = num3

  # Devuelve la lista de números de la serie
  return fib

# Ejemplo de uso
print(fibonacci(15))