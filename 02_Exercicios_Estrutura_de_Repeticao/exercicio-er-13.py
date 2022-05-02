'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

print('***********************************')
print('*************Potencia*******!******')
print('***********************************')


numero_um = int(input('Digite um numero:   '))
numero_dois = int(input('Digite outro numero:   '))

total = numero_um

for _ in range(0, numero_dois-1):
    total = total * numero_um

print(f'O resultado de {numero_um} elevado a {numero_dois} é {total}')