'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de
mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
import re

print("**********************************")
print("****FORMATAÇÃO***DE***DATA***!****")
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

    return '%d de %s de %d' % (dia, dicionario_mes[mes - 1], ano)

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

data = input('Digite uma data formatada (dd/mm/yyy):   ')
print(data_desformatada(data))