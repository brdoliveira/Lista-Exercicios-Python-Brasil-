'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as 
letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis 
tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
import random

print("*********************************")
print("****PALAVRA***EMBARALHADA***!****")
print("*********************************")

arquivo_entrada = open('arquivo.txt', 'r')


palavras = arquivo_entrada.readlines()

arquivo_entrada.close()

palavra_escolhida = palavras[
    random.randint(0, len(palavras) - 1)].upper().strip()
tamanhoPalavra = len(palavra_escolhida)
palavra_adivinhada = random.sample(palavra_escolhida, len(palavra_escolhida))
for i in palavra_adivinhada:
    print(i , end='')
print('\n\n')


palavra = input('Digite a palavra: ').upper()

if (palavra == palavra_escolhida):
    print('Voce acertou!')
else:
    print('Voce perdeu!')
    print(f'A palavra era {palavra_escolhida}')
    