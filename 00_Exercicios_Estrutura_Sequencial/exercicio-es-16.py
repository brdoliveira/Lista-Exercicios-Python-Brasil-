'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

print("**********************************")
print("****LOJA***DE***TINTAS***CORAL****")
print("**********************************")

metros_quadrados = int(input("Quantos metros quadrados voce deseja pintar?  "))

#  1 litro de tinta faz 3 metros 
quantidade_tinta = int(round(metros_quadrados / 3 , 0))

# preco da lata de tinta é 80 e vem 18 litros
preco = (quantidade_tinta / 18) * 80

quantidade_latas = 0
verificacao = metros_quadrados

while quantidade_tinta: 
    if verificacao < 54:
        quantidade_latas += 1
        break
    else:
        verificacao -= 54
        quantidade_latas += 1
        continue


print('Quantidade de tinta: {:.1f} e em dinheiro, dá R$ {:.1f} , precisará de {} lata de tinta'.format(quantidade_tinta , preco , quantidade_latas))
