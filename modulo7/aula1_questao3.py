def contar_espacos(frase):
    contador = 0
    for caractere in frase:
        if caractere == ' ':
            contador += 1
    return contador

frase = input("Digite uma frase: ")
quantidade_espacos = contar_espacos(frase)
print(f"A frase '{frase}' possui {quantidade_espacos} espaços em branco.")
