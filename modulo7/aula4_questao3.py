import re

with open("estomago.txt", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas do arquivo:")
for i in range(25):
    print(linhas[i].strip())

num_linhas = len(linhas)
print(f"\nNúmero total de linhas: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres ({len(linha_maior)} caracteres):")
print(linha_maior.strip())

nonato_count = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
iria_count = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Número de menções a 'Íria': {iria_count}")
