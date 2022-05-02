'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"
'''

print("**********************************")
print("****VITIMA***OU***NOCENTE****?****")
print("**********************************")

lista_perguntas = ('Voce telefonou para a vitima? ','Voce esteve no local do crime? ','Voce mora perto da vitima? ',
            'Voce devia para a vitima? ','Voce trabalhou para a vitima? ')

total_sim = 0

print('Responda as perguntas abaixo com S (Sim) ou N (Não)!')
for i in range(5):
    resposta = input(f'{lista_perguntas[i]}').upper()
    
    if resposta == 'S':
        total_sim += 1
        
if (total_sim < 2):
    print('Inocente')
elif (total_sim == 2):
    print('Suspeito')
elif (total_sim <= 4):
    print('Cumplice')
else:
    print('Assassino')