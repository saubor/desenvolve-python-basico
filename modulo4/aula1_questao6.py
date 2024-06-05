n = int(input("Digite a quantidade de experimentos registrados: "))

cont = 0
TotalCoelhos = 0
TotalRatos = 0
TotalSapos = 0

while n > cont:
    S=int(input("Digite a quantidade de sapos utilizados no experimento: "))
    TotalSapos= TotalSapos+S

    R=int(input("Digite a quantidade de ratos utilizados no experimento: "))
    TotalRatos= TotalRatos + R

    C=int(input("Digite a quantidade de coelhos utilizados no experimento: "))
    TotalCoelhos = TotalCoelhos + C
    cont = cont + 1

porcentagem_sapos = (TotalSapos * n) // 100
porcentagem_ratos = (TotalRatos * n) // 100
porcentagem_coelhos =(TotalCoelhos * n) // 100

print(f"Total de cobaias: {n}")
print(f"Total de coelhos: {TotalCoelhos}")
print(f"Total de ratos: {TotalRatos}")
print(f"Total de sapos: {TotalSapos}")

print(f"Percentual de coelhos: {porcentagem_coelhos}")
print(f"Percentual de sapos: {porcentagem_sapos}")
print(f"Percentual de ratos: {porcentagem_ratos}")



