'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B
seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que
a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

print('***********************************')
print('************Habitantes**!**********')
print('***********************************')


pais_a = 0
pais_b = 0

crescimento_pais_a = 0

while (pais_a <= 0):
    pais_a = int(input('Informe a populacao do pais A: '))
    if (pais_a <= 0):
        print('Populacao deve ser um valor positivo')
        
while (crescimento_pais_a <= 0):
    crescimento_pais_a = float(input('Informe o percentual de crescimento do pais A: '))
    if (crescimento_pais_a <= 0):
        print('Percentual de crescimento deve ser um valor positivo')
        
pais_b = pais_a
while (pais_b <= pais_a):
    pais_b = int(input('Informe a populacao do pais B: '))
    if (pais_b <= pais_a):
        print('Populacao do pais B deve ser maior que a populacao do pais A')
        
crescimento_pais_b = crescimento_pais_a
while (crescimento_pais_b >= crescimento_pais_a):
    crescimento_pais_b = float(input('Informe o percentual de crescimento do pais B: '))
    if (crescimento_pais_b >= crescimento_pais_a):
        print('Percentual de crescimento do pais B deve ser menor que o do pais A')

crescimento_pais_a = 1 + (crescimento_pais_a / 100.0)
crescimento_pais_b = 1 + (crescimento_pais_b / 100.0)


ano = 1
while (pais_a <= pais_b):
    pais_a *= crescimento_pais_a
    pais_b *= crescimento_pais_b
    ano += 1

print(f'Precisa de {ano} anos para que a população do pais A passe o pais B')
