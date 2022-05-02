'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''


print('*************************************')
print('**Quantidade***de***eleitores**!*****')
print('*************************************')

candidato_um = 0
candidato_dois = 0
candidato_tres = 0

quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de eleitores: '))
    if (quantidade <= 0):
        print('A quantidade deve ser positiva!')

for i in range(0, quantidade):
    print('*******1 --> Aleitor Silva*******')
    print('*******2 --> Bleitor Silva*******')
    print('*******3 --> Cleitor Silva*******')
    eleitor = int(input('Qual é o seu candidato: '))
    
    if eleitor >= 0 and eleitor <=3:
        if eleitor == 1:
            candidato_um += 1
        elif eleitor == 2:
            candidato_dois += 1
        elif eleitor == 3:
            candidato_tres +=1
        else:
            print('Algum erro apresentado ! ')
    else:
        print(' Erro na votação !')
        
print(f'\033[94m 1 --> Aleitor Silva : {candidato_um}')
print(f'\033[93m 2 --> Bleitor Silva : {candidato_dois}')
print(f'\033[95m 3 --> Cleitor Silva : {candidato_tres}')
