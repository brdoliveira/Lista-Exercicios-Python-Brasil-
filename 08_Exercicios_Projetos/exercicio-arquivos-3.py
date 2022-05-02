'''
Analisador de logs do Squid: sites bloqueados. Desenvolva um analisador de log do Squid que mostre quais os sites mais bloqueados em
uma organização.
'''

print("**********************************")
print('**ANALISADOR*DE*LOGS*DE*SQUID**!**')
print("**********************************")

bloqueados = ["bloqueado.com", "bloqueados.com"]
while True:
    site = str(input("Digite um site: "))
    if site in bloqueados:
        print("Site bloqueado!")
    else:
        print("Site liberado!")

    continuar = str(input("Digite se deseja continuar[S/N]: ")).upper().split()[0]
    if continuar in "N":
        break