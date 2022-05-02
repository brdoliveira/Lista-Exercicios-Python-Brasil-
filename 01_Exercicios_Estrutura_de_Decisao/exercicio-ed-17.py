'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto
'''

print("****************************************")
print("*****VERIFICAÇÃO****ANO****BISSEXTO*****")
print("****************************************")

ano = int(input("DIGITE O ANO ESCOLHIDO:  ")) 

verificacao_um = ano % 4 == 0 
verificacao_dois = ano % 100 != 0
verificacao_tres = ano % 400 == 0

if verificacao_um and verificacao_dois or verificacao_tres: 
    print("Ano Bissexto") 
else: 
    print("Não é um ano Bissexto!")