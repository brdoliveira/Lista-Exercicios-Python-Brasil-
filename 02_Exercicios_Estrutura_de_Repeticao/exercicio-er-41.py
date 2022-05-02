'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, 
quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
- Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25
Exemplo de saída do programa:
- Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
'''

print('***********************************************')
print('******Quantidades***de***Parcelas***!**********')
print('***********************************************')

valor_da_divida = int(input('Digite o valor da parcela:   '))
lista_parcelas = [1,3,6,9,12]
lista_porcentagem_juros = [0,0.10,0.15,0.20,0.25]
lista_valor_parcela = []

print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
for i in range(5):
    valor_juros = valor_da_divida * lista_porcentagem_juros[i]
    valor_da_parcela = valor_da_divida + valor_juros
    valor_por_parcela = valor_da_parcela / lista_parcelas[i]
    
    print('R$ {:.2f}      {}      {}       {:.2f}'.format(valor_da_parcela,valor_juros,lista_parcelas[i],valor_por_parcela))