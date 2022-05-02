'''
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''
import random

print("**********************************")
print('***EMBALHARADOR***PALAVRAS***!****')
print("**********************************")

def embaralhador(palavra):
    misturar = list(palavra)
    random.shuffle(misturar)
    misturar = "".join(misturar)
    return misturar


palavra = str(input('Digite alguma palavra:   '))


print('A palavra é {} e misturada ela fica {}'.format(palavra , embaralhador(palavra)))