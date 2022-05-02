'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre
quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando
os lançamentos dos dados.
'''
import random
import pandas as pd

print("**********************************")
print('****LANÇAMENTO***DE***DADOS***!***')
print("**********************************")

lista_numeros = []

for _ in range(100):
    dado = random.randint(1,6)
    lista_numeros.append(dado)
    
dados = pd.DataFrame({'Dados' : lista_numeros})
mostrar = dados.value_counts(sort=False)  

print(mostrar)