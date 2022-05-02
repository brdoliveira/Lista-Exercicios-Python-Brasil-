'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

import random

def imprimir_mensagem():
    print("*********************************")
    print("***Bem vindo no jogo da Forca!***")
    print("*********************************")

def carregar_palavra():
    arquivo = open("arquivo.txt","r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras(palavra_secreta):
    # Uma função define um escopo, palavras definidas na função só está visivel na função
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Digite alguma letra: ")
    chute = chute.strip().upper()
    return chute

def marcacao_de_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1 
        
def mensagem_vencedor():
    print("Você ganhou, parabéns!!")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def jogar():
    imprimir_mensagem()
    palavra_secreta = carregar_palavra()
    
    # Na variável pegam as letras da palavra_secreta e trocam por "_", depois insere no letras_acertadas
    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)
        
    enforcou = False
    acertou = False
    erros = 0
    
    # Palavras da linguagem sempre são com letras minusculas. exemplo: while , not , and , or
    # Enquanto não enforcou E não acerotu
    # Enquanto (True):
    #   Continua o loop
    while(not enforcou and not acertou):
        chute = pede_chute()
        # A variavel abaixo está usando duas funções uma está transformando tudo em maisculo e tirando os espaços caso tenha!
    
        if(chute in palavra_secreta):
           marcacao_de_chute(chute, palavra_secreta, letras_acertadas)  
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)
    print("Fim do Jogo!")


if(__name__ == "__main__"):
    jogar()
