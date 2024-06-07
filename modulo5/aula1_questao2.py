import math 
import random

n = int(input("Digite a quantidade de números: "))
soma = 0

for i in range (n):
    rando = random.randint(0, 100)
    print(rando)
    soma += rando

raiz = math.sqrt(soma)

print(raiz)

