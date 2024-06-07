import random

numero_da_vez = random.randint(0, 10)
n = 0
while n != numero_da_vez:
    n = int(input("Adivinhe o número entre 1 e 10: "))
    if n < numero_da_vez:
        print("Mais alto!")
    elif n > numero_da_vez:
        print("Mais baixo!")
    else:
        print(f"Correto, o número é {numero_da_vez}")
