'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''

print("****************************************")
print("********INTEIRO**OU**DECIMAL**!*********")
print("****************************************")

numero = float(input("Digite o numero desejado:  "))

validacao_decimal = (numero // 1 == numero)

if validacao_decimal: 
    print('Número inteiro !')
else:
    print('Número Decimal !')