distancia = (int(input("Qual a distância?")))
peso = (int(input("Qual o peso do pacote?")))



if distancia <=100:
   frete = peso * 1

if distancia > 100 and distancia <=300:
    frete = peso * 1.50

if distancia >300:
    frete = peso * 2

if peso > 10:
    frete = peso + 10


print(f"O valor do frete é {frete}")