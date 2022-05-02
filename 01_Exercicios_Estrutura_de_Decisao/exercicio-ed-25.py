'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
    e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('****************************************')
print('*****TESTE**PARTICIPAÇÃO**CRIME**!******')
print('****************************************')
print('**S -- > Sim ***************************')
print('**N -- > Não ***************************')
print('****************************************')

pergunta_um = input('Telefonou para a vítima?   ')
pergunta_dois = input('Esteve no local do crime?   ')
pergunta_tres = input('Mora perto da vítima?   ')
pergunta_quatro = input('Devia para a vítima?   ')
pergunta_cinco = input('Já trabalhou com a vítima?   ')

quantidades_sim = 0

if pergunta_um.upper() == 'S':
    quantidades_sim += 1
    
if pergunta_dois.upper() == 'S':
    quantidades_sim += 1
    
if pergunta_tres.upper() == 'S':
    quantidades_sim += 1
    
if pergunta_quatro.upper() == 'S':
    quantidades_sim += 1
    
if pergunta_cinco.upper() == 'S':
    quantidades_sim += 1
    
quantidade_zero_um = quantidades_sim == 0 or quantidades_sim == 1   
quantidade_dois = quantidades_sim == 2
quantidade_tres_quatro = quantidades_sim == 3 or quantidades_sim == 4
quantidade_cinco = quantidades_sim == 5

if quantidade_zero_um:
    print('Inocente !')
elif quantidade_dois:
    print('Suspeito...')
elif quantidade_tres_quatro:
    print('Cúmplice...')
elif quantidade_cinco:
    print('Assasino !')
    

    
    