'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
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
        if numero >= 0 and numero <= 1000:
            soma_numeros = soma_numeros + numero
            if 'maior' not in vars() or numero > maior:
                maior = numero
            elif 'menor' not in vars() or numero < menor:
                menor = numero
        else:
            print('Numero inválido')


print(f'O menor numero é {menor} e o maior é {maior} é a soma dos valores é {soma_numeros}')





