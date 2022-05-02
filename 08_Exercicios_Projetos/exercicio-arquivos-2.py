'''
Analisador de logs do Apache. Desenvolva um analisador de log do Apache que mostre quais as strings de pesquisa do google que mais levam 
internautas para o site da sua organização.
'''

print("**********************************")
print('**ANALISADOR*DE*LOGS*DO*APACHE*!**')
print("**********************************")

pesquisa1 = "Pesquisa1"
pesquisa2 = "Pesquisa2"
pesquisa3 = "Pesquisa3"
pesquisa4 = "Pesquisa4"
pesquisa5 = "Pesquisa5"
cont_1 = cont_2 = cont_3 = cont_4 = cont_5 = 0
while True:
    resultado = int(input("Digite qual das pequisas de levou ao site[ 1 / 2 / 3 / 4 / 5]: "))
    if resultado == 1:
        cont_1 += 1

    if resultado == 2:
        cont_2 += 1

    if resultado == 3:
        cont_3 += 1

    if resultado == 4:
        cont_4 += 1

    if resultado == 5:
        cont_5 += 1

    continuar = str(input("Deseja continuar[S/N]: ")).upper().split()[0]
    if continuar in "N":
        break

print("Quantidade do 1°", cont_1)
print("Quantidade do 2°", cont_2)
print("Quantidade do 3°", cont_3)
print("Quantidade do 4°", cont_4)
print("Quantidade do 5°", cont_5)