'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

print('***********************************************')
print('**Veja**a**tabuada**do**numero**escolhido**!***')
print('***********************************************')

numero_escolhido = int(input('Digite o numero escolhido:   '))


print(f' Tabuada de {numero_escolhido}:')
for i in range(1,11):
    resultado_multiplicacao = i * numero_escolhido
    print(f' {numero_escolhido} X {i} = {resultado_multiplicacao}')