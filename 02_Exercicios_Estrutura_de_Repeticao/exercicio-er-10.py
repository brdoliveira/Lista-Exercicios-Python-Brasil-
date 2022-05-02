'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''

print('*************************************')
print('**Quais**são**os**numeros**entre**!**')
print('*************************************')

numero_menor = int(input('Digite o numero menor:   '))
numero_menor += 1
numero_maior = int(input('Digite o numero maior:   '))

for i in range(numero_menor , numero_maior):
    print(i)