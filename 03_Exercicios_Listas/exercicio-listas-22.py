'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento 
nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e 
anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de
entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

print("**********************************")
print('**SUPORTE***DE***INFORMÁTICA***!**')
print("**********************************")

id_mouses = -1
defeitos = ('1 - Necessita de Esfera',
            '2 - Necessita de limpeza',
            '3 - Necessita troca de cabo ou conector',
            '4 - Quebrado ou inutilizado')
total_defeitos = [0] * 4
total_mouses = 0

for i in defeitos:
    print(i)

while (id_mouses != 0):
    id_mouses = int(input('Identificador do Mouse: '))
    if (id_mouses != 0):
        defeito = int(input('Codigo do defeito: '))
        total_defeitos[defeito - 1] += 1
        total_mouses += 1

print(f'Quantidade de mouses: {total_mouses}')

print('Situacao\tQuantidade\tPercentual')
for i in range(0, len(defeitos)):
    porcentagem = total_defeitos[i] / float(total_mouses) * 100
    print(f'{defeitos[i]}\t{total_defeitos[i]}\t{porcentagem}')