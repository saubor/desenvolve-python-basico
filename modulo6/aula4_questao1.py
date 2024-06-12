i=0
listaPar=[i for i in range (20,52) if i % 2 == 0]
print(listaPar)

quadrado =[1,2,3,4,5,6,7,8,9]
quadrado =[item**2 for item in quadrado]
print(quadrado)

lista7 = [i for i in range (1, 101) if i % 7 == 0]
print(lista7)


listaparimpar = ["par" if i % 2 ==0 else "impar" for i in range(0,30,3)]
print(listaparimpar)