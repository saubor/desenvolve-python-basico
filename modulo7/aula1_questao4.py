def formatar_numero_celular(numero):
    if len(numero) == 8:
        numero_formatado = '9' + numero
    elif len(numero) == 9:
        if numero[0] == '9':
            numero_formatado = numero[:5] + '-' + numero[5:]
        else:
            numero_formatado = numero
    else:
        numero_formatado = numero
    
    return numero_formatado


numero_celular = input("Digite o número de celular (apenas números): ")


numero_formatado = formatar_numero_celular(numero_celular)

print(f"Número de celular formatado: {numero_formatado}")
