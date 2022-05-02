'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

print("**********************************")
print("***CONTA**ESPAÇOS**E**VOGAIS**!***")
print("**********************************")

string = str(input('Digite alguma string:   ')).upper()

total_espacos = 0
total_vogais = 0

for i in string:
    if i == ' ':
        total_espacos += 1
    if (i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U'):
        total_vogais += 1
        
print(f'\
Tem {total_espacos} espaços na string \n\
Tem {total_vogais} vogais na string') 