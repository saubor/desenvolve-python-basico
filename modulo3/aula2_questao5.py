genero = input("Qual seu gênero?")
idade = (int(input("qual sua idade?")))
tempo = (int(input("Quantos anos você trabalha?")))

a= (genero == "f" and idade  >=60) or (genero == "m" and idade >=65)
b=tempo > 30
c= idade >= 60 and tempo >=25

pode_aposentar= a or b or c

print(pode_aposentar)