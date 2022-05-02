'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B
seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que
a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

print('***********************************')
print('************Habitantes**!**********')
print('***********************************')

pais_a = 80000
crescimento_pais_a = 0.03
pais_b = 200000
crescimento_pais_b = 0.015

ano = 1
while (pais_a <= pais_b):
    pais_a *= crescimento_pais_a
    pais_b *= crescimento_pais_b
    ano += 1

print(f'Precisa de {ano} anos para que a população do pais A passe o pais B')
