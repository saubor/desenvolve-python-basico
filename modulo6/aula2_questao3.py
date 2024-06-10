#3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
#  Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista

import random

lista1 = []
lista2 = []
interseccao = []

for i in range (20):
    x = random.randint(0,50)
    y = random.randint(0,50)
    lista1.append(x)
    lista2.append(y)

for i in (lista1):
    if i in lista2 and i not in interseccao:
        interseccao.append(i)

print(lista1)
print(lista2)
print(sorted(interseccao))

for i in interseccao:
    print(f"{i}: ({lista1.count(i)}) ({lista2.count(i)})")

