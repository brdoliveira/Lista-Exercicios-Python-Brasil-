'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

print('***********************************************')
print('**********Cidades***Brasileiras****!***********')
print('***********************************************')

soma_veiculos = 0
soma_acidentes = 0
soma_acidentes_menos_2mil = 0
total_acidentes_menos_2mil = 0

lista_codigo = []
lista_acidentes = []

for i in range(0,5):
    codigo = int(input('Digite o codigo da cidade:   '))
    veiculos = float(int(input('Digite o numero de veiculos de passeio:   ')))
    acidentes = int(input('Digite a quantidade de acidentes em 1999:   '))
    
    lista_codigo.append(codigo)
    
    indice_acidentes  = acidentes / veiculos
    lista_acidentes.append(acidentes)
    soma_veiculos += veiculos
    
    if (veiculos < 2000):
        soma_acidentes_menos_2mil += acidentes
        total_acidentes_menos_2mil += 1


mais_acidentes = max(lista_acidentes)
codigo_mais_acidentes = lista_codigo[lista_acidentes.index(mais_acidentes)]

menos_acidentes = min(lista_acidentes)
codigo_menos_acidentes = lista_codigo[lista_acidentes.index(menos_acidentes)]

media = soma_veiculos / 5
media_2k = soma_acidentes_menos_2mil / total_acidentes_menos_2mil

print(f'A cidade com mais acidentes é {codigo_mais_acidentes} com {mais_acidentes} acidentes \n\
A cidade com menos acidentes é {codigo_menos_acidentes} com {menos_acidentes} acidentes \n\
A media de veiculos por cidade é {media} , e a media com menos de 2mil veiculos é {media_2k}')



    
    