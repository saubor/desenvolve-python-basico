n = int(input("Digite a quantidade de respondentes: "))


soma_idade = 0
cont = 0

while  n > cont:
    idade= int(input("Digite a idade do respondente: "))
    soma_idade += idade 
    cont = cont + 1

média = soma_idade/n

print(f"A idade média dos respondentes é {média}")