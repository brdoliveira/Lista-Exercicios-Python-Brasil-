'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

print('*************************************')
print('***Quantidade***de***CDs***!*********')
print('*************************************')

quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Voce quer saber a media do valor gasto de qunatos CD´s: '))
    if (quantidade <= 0):
        print('A quandidade deve ser positiva!')

soma = 0.0
for i in range(0, quantidade):
    quantidade_cd = float(input(f'Informe o valor do {i + 1}º CD: '))
    soma += quantidade_cd


media = soma / quantidade
print(f'A media dos CDs é {media}')