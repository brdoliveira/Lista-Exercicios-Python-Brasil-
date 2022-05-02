'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

print("**********************************")
print('*****COMPARAÇÃO***STRINGS***!*****')
print("**********************************")

string_um = str(input('Digite a primeira string:   '))
string_dois = str(input('Digite a segunda string:    '))

print(f'A primeira string "{string_um}" : {len(string_um)}')
print(f'A segunda string "{string_dois}" : {len(string_dois)}')

if len(string_um) == len(string_dois):
    print('As strings TEM o mesmo tamanho !')
else:
    print('As strings NÃO TEM o mesmo tamanho !')


if string_dois == string_um:
    print('As strings TEM o mesmo conteúdo !')
else:
    print('As strings NÃO TEM o mesmo conteúdo !')