'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre 
este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor 
a ser pago pelo cliente.
'''

print('****************************************')
print('********MORANGO***OU***MAÇA***!*********')
print('****************************************')

quantidade_morango = int(input('Digite o valor de morango:   '))
quantidade_maca = int(input('Digite o valor de maca:   '))

if quantidade_morango <= 5:
    valor_morango = quantidade_morango * 2.5
else:
    valor_morango = quantidade_morango * 2.2
    
if quantidade_maca <= 5:
    valor_maca = quantidade_maca * 2.2
else:
    valor_maca = quantidade_maca * 1.5
    
valor_total = valor_morango + valor_maca
quantidade_total = quantidade_maca + quantidade_morango

if valor_total >= 25 or quantidade_total >= 8:
    valor_total = valor_total * 0.9
    print(' Total a ser pago é R$ {:.1f}'.format(valor_total))    
else:
    print(' Total a ser pago é R$ {:.1f}'.format(valor_total))    