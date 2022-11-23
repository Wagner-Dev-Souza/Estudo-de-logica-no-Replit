#coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
#lista
precos = [20,50,200]
#indices   0  1  2

#localizar por indice:
print(precos[0])
#localizar o indice:
print(precos.index(200))
#lista pode conter strings, valores inteiros ou boleanos na mesma lista:
diversidades = [15,'Wagner',True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

#Laços em iteráveis
for preco in precos:
  print(preco)
'''
Exemplo - Some os valores:
Dado uma coleção de dados "idades" [15,46,75,34,23], imprima na tela a soma destes valores

idades = [15,46,75,34,23]
total = 0
loop idade em idades
  total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
  total = total + idade
print(total)