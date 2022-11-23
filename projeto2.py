'''
Escreva um programa que , ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleátorio gerado no início do programa seja chutado corretamente.
O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado.

# Método 5Q's para montar um algorítimo:
Analise criticamente o problema e descubra:
(Tenete explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
  -valor aleatório de 1 a 10. um chute do usuário
2. O que devo fazer com esses dados?
  -eu devo comparar os números.
3. Quais são as restrições deste problema?
  -número de 1 a 10
4. Qual é o resultado esperado?
  -exibir se o chute foi acima, abaixo ou igual ao valor gerado
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
  print "Chute foi maior que o valor gerado"
if chute < valor_aleatorio
  print "Chute foi menor que o valor gerado" 
if chute = valor aleatorio
  print "Você acertou!!!"

'''
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maior que o gerado')
  elif chute < valor_aleatorio:
    print('Cute foi menor que o gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!!!')
