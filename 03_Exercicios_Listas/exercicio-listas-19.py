'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e 
informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''


print("**********************************")
print("***SERVIDORES**OPERACIONAIS***!***")
print("**********************************")

sistema_opecional = (
    'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro')
votos = [0] * 6
opcao = -1
print('Qual o melhor Sistema Operacional para uso em servidores?')
print('\nAs possiveis respostas sao:\n')

i = 0
for sistema in sistema_opecional:
    print('%d- %s' % (i + 1, sistema_opecional[i]))
    i += 1

while (opcao != 0):
    opcao = int(input('Sistema escolhido (0=fim): '))
    if (opcao < 0) or (opcao > 23):
        print('Informe um valor entre 1 e 6 ou 0 para sair!')
        continue
    if (opcao != 0):
        votos[opcao - 1] += 1

print('Sistema Operacional   Votos   %')
print('-------------------   -----   ------')
i = 0
maiorVoto = 0
for sistema in sistema_opecional:
    print('%-21s %5d   %2.2f' %\
        (sistema_opecional[i], votos[i],
         votos[i] / float(sum(votos)) * 100))
    if (votos[i] > votos[maiorVoto]):
        maiorVoto = i
    i += 1
print('-------------------   -----')
print('Total                   %3d' % sum(votos))

print('O sistema operacional mais votado foi o %s, com %d, correspondendo a '\
    '%.2f%% dos votos.' %\
    (sistema_opecional[maiorVoto], votos[maiorVoto],
        votos[maiorVoto] / float(sum(votos)) * 100))