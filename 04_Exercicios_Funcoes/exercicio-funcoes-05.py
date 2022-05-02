'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para 
incluir o imposto sobre vendas.
'''

print("**********************************")
print('*********SOMA**IMPOSTO**!*********')
print("**********************************")

def somaImposto(taxaImposto,custo):
    taxaImposto = taxaImposto * custo / 100.0
    custoImposto = custo + taxaImposto
    return custoImposto

c = float(input('Digite o custo do produto:        '))
i = float(input('Digite a porcentagem do imposto:  '))

print(f'O novo custo é {somaImposto(i,c)}')