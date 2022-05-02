'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
   uma nota de 5 e quatro notas de 1.
'''

print("****************************************")
print("*********CAIXA***ELETRONICO***!*********")
print("****************************************")

valor = int(input("Digite o valor desejado:  "))

if (valor < 10) or (valor > 600):
   print('Valor invalido para saque')
else:
   notas_100 = valor // 100
   verificacao_100 = (valor - (notas_100 * 100))
   
   notas_50 = verificacao_100 // 50
   verificacao_50 = (valor - (notas_100 * 100) - (notas_50 * 50))
   
   notas_10 = verificacao_50 // 10
   verificacao_10 = (valor - (notas_100 * 100) - (notas_50 * 50) - (notas_10 * 10))
   
   notas_5 = verificacao_10 // 5
   verificacao_5 = valor - (notas_100 * 100) - (notas_50 * 50) - (notas_10 * 10) - (notas_5 * 5)
   
   notas_1 = verificacao_5

print(f'Notas de 100: {notas_100} , resultando R${notas_100 * 100}')
print(f'Notas de  50: {notas_50} , resultando R${notas_50 * 50}')
print(f'Notas de  10: {notas_10}, resultando R${notas_10 * 10}')
print(f'Notas de   5: {notas_5} , resultando R${notas_5 * 5}')
print(f'Notas de   1: {notas_1} , resultando R${notas_1 * 1} ')