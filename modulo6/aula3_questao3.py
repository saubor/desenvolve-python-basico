import random

lista = [random.randint(-10, 10) for _ in range(20)]

def encontrar_intervalo_negativos(lista):
    max_negativos = 0
    intervalo_inicio = 0
    intervalo_fim = 0

    for i in range(len(lista)):
        for j in range(i, len(lista)):
            sub_lista = lista[i:j+1]
            negativos = sum(1 for x in sub_lista if x < 0)
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo_inicio = i
                intervalo_fim = j

    return intervalo_inicio, intervalo_fim

inicio, fim = encontrar_intervalo_negativos(lista)
lista_original = lista.copy()
del lista[inicio:fim+1]

print("Original:", lista_original)
print("Editada:", lista)
