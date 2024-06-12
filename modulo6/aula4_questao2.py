frase = input("Digite uma frase: ")

vogais = 'aeiouAEIOU'
lista_vogais = sorted([char for char in frase if char in vogais])
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {lista_consoantes}")
