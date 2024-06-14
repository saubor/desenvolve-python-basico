import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []
    
    for palavra in palavras:
        if len(palavra) > 2:
            letras_interiores = list(palavra[1:-1])
            random.shuffle(letras_interiores)
            palavra_embaralhada = palavra[0] + ''.join(letras_interiores) + palavra[-1]
        else:
            palavra_embaralhada = palavra
        
        frase_embaralhada.append(palavra_embaralhada)
    
    return ' '.join(frase_embaralhada)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)

