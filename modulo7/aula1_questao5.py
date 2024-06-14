def contar_vogais_e_indices(frase):
    vogais = "aeiou"
    indices_vogais = []
    quantidade_vogais = 0
    
    for indice, letra in enumerate(frase):
        if letra.lower() in vogais:
            quantidade_vogais += 1
            indices_vogais.append(indice)
    
    return quantidade_vogais, indices_vogais

frase = input("Digite uma frase: ")

quantidade_vogais, indices_vogais = contar_vogais_e_indices(frase)

print(f"A frase '{frase}' possui {quantidade_vogais} vogais.")
print("Índices das vogais na frase:", indices_vogais)
