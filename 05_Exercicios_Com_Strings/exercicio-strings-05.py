'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
'''

print("**********************************")
print('*NOME**NA**VERTICA**EM**ESCADA**!*')
print("**********************************")

string = str(input('Digite uma string:   '))

for i in range(len(string)):
    print(string[:(len(string)- i)])