'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado
de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar
jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

import random

print("**********************************")
print("******JOGO***DE***CRAP'S***!******")
print("**********************************")

def jogo_de_craps():
    jogada = random.randint(2,12)
    return jogada

acabou_jogo = False

quantidade_jogos = 1

while not acabou_jogo:
    jogada = jogo_de_craps()
    print(f'{quantidade_jogos}° jogada: {jogada}')
    
    if quantidade_jogos == 1:
        if (jogada == 7) or (jogada == 11):
            acabou_jogo = True
            print('Ganhou')
        elif (jogada == 2) or (jogada == 3) or (jogada == 13):
            acabou_jogo = True 
            print('Crap´s! Perdeu! ;-;')
        else:
            pontos = jogada
    else:
        if jogada == 7:
            print('Você Perdeu! ;-;')
            acabou_jogo = True
        elif jogada == pontos:
            print('Voce ganhou !!! ')
            acabou_jogou = True
    quantidade_jogos += 1
            
            