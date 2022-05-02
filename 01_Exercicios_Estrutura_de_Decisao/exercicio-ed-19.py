'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

print("****************************************")
print("******PROGRAMA***LER***NUMEROS***!******")
print("****************************************")

n = int(input("DIGITE O NUMERO: "))

if n < 1000:
    centenas = n /100
    print('Centenas:',int(centenas))

    dezenas = (n - (int(centenas) * 100)) / 10
    print('Dezenas:', int(dezenas))

    unidades = n - (int(centenas) * 100) - (int(dezenas) * 10)
    
    print(f'Unidades: {unidades}')    