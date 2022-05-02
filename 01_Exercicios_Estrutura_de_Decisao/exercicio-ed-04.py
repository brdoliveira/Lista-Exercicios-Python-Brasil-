'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

print("****************************************")
print("**********DIGITE**UMA**LETRA*!**********")
print("****************************************")

letra_inserida = input("DIGITE A LETRA ESCOLHIDA:  ")
letra_inserida = letra_inserida.upper()

if letra_inserida == "A" or letra_inserida == "E" or letra_inserida == "I" or letra_inserida == "O" or letra_inserida == "U":
    print("UMA VOGAL FOI INSERIDA !")
else:
    print("UMA CONSOANTE FOI INSERIDA !")