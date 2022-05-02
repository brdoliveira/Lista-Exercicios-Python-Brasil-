'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
--Álcool:
a. até 20 litros, desconto de 3% por litro
b. acima de 20 litros, desconto de 5% por litro
--Gasolina:
a. até 20 litros, desconto de 4% por litro
b. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
   (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
   preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

print('****************************************')
print('******ALCOOL***OU***GASOLINA***!********')
print('****************************************')
print('** A -- > Álcool ***********************')
print('** G -- > Gasolina *********************')
print('****************************************')

alcool_gasolina = input('QUAL VOCE DESEJA:   ')
quantidade_litro = int(input('QUANTOS LITROS:   '))

verificacao_alcool = alcool_gasolina.upper() == 'A'
verificacao_gasolina = alcool_gasolina.upper() == 'G'

preco_litro = 0
desconto = 0 

if verificacao_alcool:
    preco_litro = 1.9
    if quantidade_litro <= 20:
        desconto = 0.03
    elif quantidade_litro > 20:
        desconto = 0.05 
    
elif verificacao_gasolina:
    preco_litro = 2.5
    if quantidade_litro <= 20:
        desconto = 0.04
    elif quantidade_litro > 20:
        desconto = 0.06
        
else:
    print('ERROR !')
        
preco_final = quantidade_litro * (preco_litro + (preco_litro * desconto))
print(f'Valor: R$ {preco_final}')