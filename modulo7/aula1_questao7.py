import random

def encrypt(lista_strings):
    
    n = random.randint(1, 10)
    
    
    nomes_criptografados = []
    
    for string in lista_strings:
        nome_criptografado = []
        for char in string:
            if 33 <= ord(char) <= 126:
                
                novo_char = chr((ord(char) - 33 + n) % 94 + 33)
                nome_criptografado.append(novo_char)
            else:
                
                nome_criptografado.append(char)
        
       
        nomes_criptografados.append(''.join(nome_criptografado))
    
    
    return nomes_criptografados, n


lista_nomes = ["Fulano", "Beltrano", "Ciclano"]

nomes_criptografados, chave = encrypt(lista_nomes)

print("Nomes Criptografados:")
for nome in nomes_criptografados:
    print(nome)

print(f"\nChave de criptografia: {chave}")
