'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o 
usuário digite o salário inicial do funcionário.
'''
print('***********************************************')
print('*******Percentual**do***Reajuste****!*******')
print('***********************************************')

salario = 1000.0
percentual = 1.5
ano = 1996

while (ano <= 2021):
    print(f'Ano {ano} Percentual {percentual} Salario {salario}')
    salario += (salario * (percentual / 100.0))
    percentual *= 2
    ano += 1

print(f'Salario atual do funcionario: {salario}')