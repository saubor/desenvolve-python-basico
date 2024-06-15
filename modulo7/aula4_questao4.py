import random


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read().splitlines()


def imprime_enforcado(erros, estagios_enforcado):
    print(estagios_enforcado[erros])


def jogo_da_forca():
    
    palavras = ler_arquivo('gabarito_forca.txt')
    
    
    palavra = random.choice(palavras).lower()
    
    
    estagios_enforcado = ler_arquivo('gabarito_enforcado.txt')
    
    
    palavra_oculta = ['_'] * len(palavra)
    letras_erradas = []
    tentativas_restantes = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    print(' '.join(palavra_oculta))
    
    
    while tentativas_restantes > 0 and '_' in palavra_oculta:
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue
        
        if letra in palavra_oculta or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if letra in palavra:
            print("Boa! A letra", letra, "está na palavra.")
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            print("Que pena! A letra", letra, "não está na palavra.")
            letras_erradas.append(letra)
            tentativas_restantes -= 1
            imprime_enforcado(len(letras_erradas), estagios_enforcado)
        
        print(' '.join(palavra_oculta))
        print("Letras erradas:", ' '.join(letras_erradas))
        print("Tentativas restantes:", tentativas_restantes)
    
    if '_' not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra:", palavra)
    else:
        print("Fim de jogo! A palavra era:", palavra)


jogo_da_forca()
