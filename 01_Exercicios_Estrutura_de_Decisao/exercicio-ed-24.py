'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

print('****************************************')
print('*****RESULTADO**DA**OPERAÇÃO**!*********')
print('****************************************')
print('** 1 - Par ou Impar ********************')
print('** 2 - Positivo ou Negativo ************')
print('** 3 - Inteiro ou Decimal **************')

escolha = float(input('Digite a função desejada:  '))
numero = float(input('Digite o numero desejado:  '))

if escolha == 1:
    validacao_par = numero % 2 == 0
    if validacao_par:
        print('Numero é par !')
    else:
        print('Numero é impar !')
        
elif escolha == 2:
    validacao_positivo = numero >= 0
    if validacao_positivo:
        print('Numero é positivo !')
    else:
        print('Numero é negativo !')
elif escolha == 3:
    validacao_decimal = (numero // 1 == numero)
    if validacao_decimal: 
        print('Número inteiro !')
    else:
        print('Número Decimal !')
else:
    print('Essa opção não existe !')