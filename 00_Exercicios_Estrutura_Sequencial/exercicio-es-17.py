'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

print("**********************************")
print("****LOJA***DE***TINTAS***CORAL****")
print("**********************************")

metros_quadrados = int(input("Quantos metros quadrados voce deseja pintar?  "))

#  1 litro de tinta faz 3 metros 
quantidade_tinta = int(round(metros_quadrados / 6 , 0))

quantidade_latas_18 = 0
quantidade_latas_36= 0
quantidade_latas_ambas_36 = 0

verificacao_36 = metros_quadrados
verificacao_18 = metros_quadrados
verificacao_ambos = metros_quadrados

while quantidade_tinta: 
    if verificacao_36 <= 22:
        quantidade_latas_36 += 1
        break
    else:
        verificacao_36 -= 22
        quantidade_latas_36 += 1
    
while quantidade_tinta: 
    if verificacao_18 < 108:
        quantidade_latas_18 += 1
        verificacao_ambos = verificacao_18
        break
    else:
        verificacao_18 -= 108
        quantidade_latas_18 += 1

while quantidade_tinta:
    if verificacao_ambos <= 22:
        quantidade_latas_ambas_36 += 1
        break
    else:
        verificacao_ambos -= 22
        quantidade_latas_ambas_36 += 1
    

quantidade_mescla = (quantidade_latas_18 * 80) + (quantidade_latas_ambas_36 * 25)    

print(f'Precisará de {quantidade_latas_18} lata de tinta de 18L dando R$ {(quantidade_latas_18 * 80)}, ou {quantidade_latas_36} de 3.6L dando R$ {(quantidade_latas_36 * 25)} , e comprando as duas {quantidade_latas_18} de 18L e {quantidade_latas_ambas_36} de 3.6L, dando R$ {quantidade_mescla}')
