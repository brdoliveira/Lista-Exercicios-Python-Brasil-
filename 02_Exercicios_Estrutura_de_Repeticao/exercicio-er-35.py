'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número 
inteiro informado pelo usuário.
'''

print('*************************************')
print('*******Numeros***Primo*****!*********')
print('*************************************')

quantidade = 0
lista_primos = []
while (quantidade <= 0):
    quantidade = int(input('Voce quer saber os primeiros quantos numeros: '))
    if (quantidade <= 0):
        print('A quantidade deve ser positiva!')

quantidadeDivisoes = 0
for numero in range(1, quantidade + 1):
    primo = True
    for i in range(2, numero):
        if (numero % i == 0):
            primo = False
            break

    if (primo):
        quantidadeDivisoes += 1
        lista_primos.append(numero)

print(f'Quantidade de divisoes: {quantidadeDivisoes} e os numeros são {lista_primos}' )