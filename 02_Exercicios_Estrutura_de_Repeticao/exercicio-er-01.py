'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido.
'''

print('***********************************')
print('*INSIRA**UMA**NOTA**(ENTRE*0*E*10)*')
print('***********************************')

nota = 100
while (nota < 0) or (nota > 10):
    nota = int(input('Informe uma nota: '))
    if (nota < 0) or (nota > 10):
        print('Nota Invalida')