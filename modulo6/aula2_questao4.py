#4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
#  Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista.
#  Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

lista1 = []
lista2 = []
intercalada = []


x = int(input("Digite a quantidade de itens na lista 1: "))

for i in range (x):
    lista1.append(int(input()))


y = int(input("Digite a quantidade de itens da lista 2: "))

for i in range (y):
    lista2.append(int(input()))

comprimento_max = max(len(lista1), len(lista2))

# Itera até o comprimento máximo
for i in range(comprimento_max):
    if i < len(lista1):
        intercalada.append(lista1[i])
    if i < len(lista2):
        intercalada.append(lista2[i])

print(intercalada)