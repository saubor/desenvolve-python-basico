#Definindo o tamnho do terreno e o preço do metro quadrado
comprimento = (int(input("Qual o comprimento do terreno? ")))
largura = (int(input("Qual a largura do terreno? ")))
preço_m2 = (float(input("Qual o preço do m2?")))

#formulas para encontrar a area do terreno e o preço total
area_m2 = comprimento * largura
preco_total = preço_m2 * area_m2

#Saída de dados mostrando o tamanho completo do terreno e seu preço.
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.3f}")