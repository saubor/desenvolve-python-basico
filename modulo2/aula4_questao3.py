nome_produto1=input("Digite o nome do produto 1: ")
preço_produto1= (float(input("Digite o preço unitário do produto 1: ")))
quantidade_produto1=(float(input("Digite a quantidade do produto 1: ")))
total1= preço_produto1 * quantidade_produto1

nome_produto2=input("Digite o nome do produto 2: ")
preço_produto2=(float(input("Digite o preço unitário do produto 2: ")))
quantidade_produto2=(float(input("Digite a quantidade do produto 2: ")))
total2= preço_produto2 * quantidade_produto2

nome_produto3=input("Digite o nome do produto 3: ")
preço_produto3=(float(input("Digite o preço unitário do produto 3: ")))
quantidade_produto3=(float(input("Digite a quantidade do produto 3: ")))
total3= preço_produto3 * quantidade_produto3

total_completo= total1 + total2 + total3



print(f"Total: {total_completo:,.2f} R$")

