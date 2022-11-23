# Condicionais
# if, elif e else

'''
# primeira parte
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode entrar, caso contrário estará suspenso.
'''

numero_de_atrasos = input ("Digite o número de atrasos.")
if int(numero_de_atrasos) >= 3:
  print('Você está suspenso!')
elif int(numero_de_atrasos) == 1:
  print('Pode entrar, mas caso se atrase mais 2 vezes, você será suspenso. Fique atento!')
elif int(numero_de_atrasos) == 2:
  print('Pode entrar, mas cuidado, caso você se atrase novamente, será suspenso. Não de bobeira!')
else:
  print ('Pode entrar!!!')


'''
#segunda parte
encontre o maior entre dois números

input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
print o primeiro valor é maior
else
print o segundo valor é maior
'''

primeiro_valor = input('Digite o 1º valor: ')
segundo_valor = input('Digite o 2º valor: ')
if int (primeiro_valor) > int(segundo_valor):
  print('O primeiro valor é maior!')
else:
  print('O segundo valor é maior!')