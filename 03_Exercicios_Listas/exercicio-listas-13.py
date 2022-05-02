'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual 
das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

print("**********************************")
print("**TEMPERATURA***DOS***MESES***!***")
print("**********************************")

meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
lista_temperaturas = []

for m in range(12):
    temperaturas = float(input(f'Informe a temperatura media do mes ({meses[m]}):   '))
    lista_temperaturas.append(temperaturas)
    
media = sum(lista_temperaturas) / 12

print(f'A media das temperaturas é {media:.2f}')

for i in range(12):
    if(lista_temperaturas[i] >= media):
        print(f'{meses[i]} - {lista_temperaturas[i]}')