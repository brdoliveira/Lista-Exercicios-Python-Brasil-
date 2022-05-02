'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
    1 , 2, 3, 4  - Votos para os respectivos candidatos 
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

print('*************************************')
print('***Eleição***dos***anos***2000***!***')
print('**** 1 - José                    ****')
print('**** 2 - João                    ****')
print('**** 3 - Pedro                   ****')
print('**** 4 - Cleber                  ****')
print('**** 5 - Voto Nulo               ****')
print('**** 6 - Voto em Branco          ****')
print('*************************************')

votos = 1
voto_um = 0
voto_dois = 0
voto_tres = 0
voto_quatro = 0
voto_nulo = 0
voto_branco = 0
quantidade_votos = 0


while (votos >= 1 and votos <= 6):
    voto_digitado = int(input('Digite o voto:   '))
    
    if voto_digitado == 1:
        voto_um += 1
        quantidade_votos += 1
    elif voto_digitado == 2: 
        voto_dois += 1
        quantidade_votos += 1
    elif voto_digitado == 3:
        voto_tres += 1
        quantidade_votos += 1
    elif voto_digitado == 4: 
        voto_quatro += 1
        quantidade_votos += 1
    elif voto_digitado == 5:
        voto_nulo += 1
        quantidade_votos += 1
    elif voto_digitado == 6:
        voto_branco += 1
        quantidade_votos += 1
    votos = voto_digitado
            
porcentagem_nulo = (voto_nulo * 100 / quantidade_votos)
porcentagem_branco = (voto_branco / quantidade_votos * 100)
print(voto_branco)
print(porcentagem_nulo)
print(porcentagem_branco)
            
print(f' Votos candidato 1: {voto_um}')
print(f' Votos candidato 2: {voto_dois}')
print(f' Votos candidato 3: {voto_tres}')
print(f' Votos Nulos: {voto_nulo} - {porcentagem_nulo}')
print(f' Votos em Branco: {voto_branco} - {porcentagem_branco} ')