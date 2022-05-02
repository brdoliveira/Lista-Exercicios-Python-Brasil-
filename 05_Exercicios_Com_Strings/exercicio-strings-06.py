'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso.
'''

import re

print("**********************************")
print("****DATA***DE***NASCIMENTO***!****")
print("**********************************")

def data_desformatada(data):
    reg = re.compile('^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$') #REGEX
    if (not (reg.match(data))):
        print('Data invalida')
        return None

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if (not validade(dia, mes, ano)):
        return None

    dicionario_mes = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
                  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

    return 'Você nasce em %d de %s de %d' % (dia, dicionario_mes[mes - 1], ano)

def validade(dia, mes, ano):
    if (dia < 0) or (dia > 31):
        return False

    meses = (4, 6, 9, 11)
    if (mes in meses):
        if (dia > 30):
            return False

    if (mes == 2):
        if (dia > 28):
            if (ano % 4 != 0):
                return False
            elif (ano % 100 == 0) and (ano % 1000 != 0):
                return False
    return True

data = input('Data de Nascimento: :   ')
print(data_desformatada(data))