def contar_caracteres(palavra):
    contador = {}
    for letra in palavra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

def encontrar_anagramas_na_frase(frase, objetivo):
    objetivo_contador = contar_caracteres(objetivo.lower())
    objetivo_length = len(objetivo)
    
    palavras = frase.lower().split()
    palavras = [palavra.strip('.,!?') for palavra in palavras]
    
    anagramas = []
    
    for palavra in palavras:
        if len(palavra) == objetivo_length:
            palavra_contador = contar_caracteres(palavra)
            
            if palavra_contador == objetivo_contador:
                anagramas.append(palavra)
    
    return anagramas


frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")


anagramas = encontrar_anagramas_na_frase(frase, objetivo)


print(f"Anagramas: {anagramas}")
