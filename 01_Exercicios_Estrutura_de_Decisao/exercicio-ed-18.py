'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

print("****************************************")
print("*****VERIFICAÇÃO****DE****DATA****!*****")
print("****************************************")

data_inserida = input("DIGITE A DATA ESCOLHIDA:  ")
# 12/03/1999

dia = int(data_inserida[0:2])
mes = int(data_inserida[3:5])
ano = data_inserida[6:]

verificacao_dia = (dia >= 1 and dia <= 31)
verificacao_mes = (mes >= 1 and mes <= 12)
verificacao_ano = len(ano) == 4


if verificacao_dia and verificacao_mes and verificacao_ano:
    print("Data Válida !")
else:
    print("Data Inválida !")