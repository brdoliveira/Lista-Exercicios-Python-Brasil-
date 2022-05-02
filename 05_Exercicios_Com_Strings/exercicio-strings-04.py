'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
'''

print("**********************************")
print('*NOME**NA**VERTICA**EM**ESCADA**!*')
print("**********************************")

string = str(input('Digite uma string:   '))

for i in range(0,len(string) + 1):
    print(string[:i])