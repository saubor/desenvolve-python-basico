import re

def eh_palindromo(frase):
    
    frase_tratada = re.sub(r'[^a-zA-Z]', '', frase).lower()
    
    return frase_tratada == frase_tratada[::-1]

def main():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        if frase.lower() == 'fim':
            break
        
        if eh_palindromo(frase):
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

if __name__ == "__main__":
    main()
