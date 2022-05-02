'''
51- Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
'''

print('*********************************************')
print("*S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m*")
print('*********************************************')

numero = int(input('Digite o número: '))
soma = 0
denominador = 1
for i in range(1, numero + 1):
    soma += i / denominador
    denominador += 2
print(f'Soma da sequência: {soma:.2f}')