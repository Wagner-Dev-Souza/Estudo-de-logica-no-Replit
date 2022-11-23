# Laços de repetição + Listas

for palavra in range(1,4):
  print('Carregando')
'''
for item in coleção:
  expressão
'''
for item in range(1,21):
  print(item)
for item in range(1,20,2):
  print(item)

nomes = ['jhonatan','cristian','roberto','camila']
for nome in nomes:
  print(nome)

'''
#Problema
imprima os valores de 1 a N
'''

valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo+1):
  print(numero)