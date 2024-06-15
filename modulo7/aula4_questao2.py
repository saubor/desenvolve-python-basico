import re

arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

with open(arquivo_entrada, "r") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)

with open(arquivo_saida, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

with open(arquivo_saida, "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
