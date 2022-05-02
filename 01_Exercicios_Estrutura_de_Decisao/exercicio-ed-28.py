'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário 
e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

'''


print('****************************************')
print('*****HIPERMERCADO***TABAJARA***!********')
print('****************************************')
print('** 1 - File Duplo **********************')
print('** 2 - Alcatra *************************')
print('** 3 - Picanha *************************')
print('****************************************')

tipo_carne = int(input('Digite a carne que você deseja:   '))
quantidade = float(input('Digite a quantidade em quilos:   '))
tem_cartao = (input('Tem cartão tabajara? (S/N) :   ')).upper()

if tipo_carne == 1:
    carne_escolhida = "Filé Duplo"
    if quantidade <= 5:
        valor = quantidade * 4.9
    else:
        valor = quantidade * 5.8
        
elif tipo_carne == 2:  
    carne_escolhida = "Alcatra"
    if quantidade <= 5:
        valor = quantidade * 5.9
    else:
        valor = quantidade * 6.8
        
elif tipo_carne == 3:
    carne_escolhida = "Picanha"
    if quantidade <= 5:
        valor = quantidade * 6.9
    else:
        valor = quantidade * 7.8
        
if tem_cartao == 'S':
    valor = valor * 0.95
    print(' A carne escolhida foi {} e foi pedido {} quilos , dando R$ {:.2f}'.format(carne_escolhida, quantidade, valor))
elif tem_cartao == 'N':
    print(' A carne escolhida foi {} e foi pedido {} quilos , dando R$ {:.2f}  \n\
    Aproveite e faça nosso cartão !!!'.format(carne_escolhida, quantidade, valor))
else:
    print('Erro apresentado !')

