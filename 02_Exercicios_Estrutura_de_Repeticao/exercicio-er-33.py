'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de 
temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''

print('*************************************')
print('********Temperatura********!*********')
print('*************************************')

quantidade_temperaturas = int(input('Digite a quantidade de temperaturas:   '))
lista_temperaturas = []

for i in range(1, (quantidade_temperaturas +1)):
    temperatura = float(input(f'Digite a {i}º temperatura:   '))
    lista_temperaturas.append(temperatura)
    
maior_temperatura = max(lista_temperaturas)
menor_temperatura = min(lista_temperaturas)
media_temperatura = sum(lista_temperaturas) / len(lista_temperaturas)
    
print(f'A maior temperatura é {maior_temperatura} \n\
A menor temperatura é {menor_temperatura} \n\
A média das temperaturas é {media_temperatura}')