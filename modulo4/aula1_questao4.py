n = int(input("Digite um número: "))
maior = 0

while n > maior:
    x = int(input("Digite outro número: "))
    while x > maior:
        maior = x
    n = n - 1
print(maior)