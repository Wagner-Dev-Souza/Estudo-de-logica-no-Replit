'''
Crie um programa que recebe um número e imprime o fatorial daquele número

# Método 5Q's para montar um algorítimo:
Analise criticamente o problema e descubra:
(Tenete explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
  -um número
2. O que devo fazer com esses dados?
  -eu devo calcular o fatorial desse número e exibir na tela
3. Quais são as restrições deste problema?
  -o número deve ser positivo e inteiro
4. Qual é o resultado esperado?
  -a exibição do fatorial do número providenciado
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input numero
if numero > 0
if numero == inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero
print(fatorial)
'''

numero = int(input("Digite um número: "))
if numero > 0:
  fatorial = 1
  for item in range(1,numero+1):
    fatorial = fatorial * item
print(fatorial)
