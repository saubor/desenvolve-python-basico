import random 

x = random.randint(5, 10)
list = []

for i in range (x):
    y = int(input("Digite um numero"))
    list.append(y)

numeros_pares = [num for num in list if num % 2 == 0]
numeros_impares = [num for num in list if num % 2 != 0]


print(list)
print(list[0:3])
print(list[:3:-1])
print(list[::-1])
print(numeros_pares)
print(numeros_impares)
