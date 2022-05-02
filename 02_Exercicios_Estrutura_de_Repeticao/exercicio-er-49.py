'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

print('*************************************')
print('*****SOMA*****DA*****SERIE*****!*****')
print('*************************************')

termos = int(input('Informe a quantidade de termos que deseja: '))

valor_soma = 0.0
denominador = 1
for i in range(1, termos + 1):
    valor_soma += i / denominador
    denominador += 2

print('Resultado: {:.2f}'.format(valor_soma))