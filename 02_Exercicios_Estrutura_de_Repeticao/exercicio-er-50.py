'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''

print('*************************************')
print('*****SOMA*****DA*****SERIE*****!*****')
print('*************************************')

termos = int(input('Informe a quantidade de termos que deseja: '))

s = 0.0
for i in range(1, termos + 1):
    s += 1 / i

print('Resultado: {:.2f}'.format(s))