'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

print('*************************************')
print('***********Conjunto********!*********')
print('*************************************')

numero_repeticoes = -1
soma_numeros = 0



while numero_repeticoes < 0:
    numero_repeticoes = int(input('Informe o numero de repeticoes:   '))
    if numero_repeticoes < 0:
        print('O numero de repeticoes deve ser maior que 0 !')

    for x in range(0, numero_repeticoes):
        numero = int(input('Digite um numero:   '))
        soma_numeros = soma_numeros + numero
        if 'maior' not in vars() or numero > maior:
            maior = numero
        elif 'menor' not in vars() or numero < menor:
            menor = numero

print(f'O menor numero é {menor} e o maior é {maior} é a soma dos valores é {soma_numeros}')