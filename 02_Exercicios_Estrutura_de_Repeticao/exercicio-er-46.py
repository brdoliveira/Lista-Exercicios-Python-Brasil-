'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, 
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer
um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''
print('*************************************')
print('**************ATLETA****!************')
print('*************************************')

nomeAtleta = ' '

while (nomeAtleta != ''):
    nomeAtleta = input('Atleta: ')

    if (nomeAtleta != ''):
        primeiroSalto = float(input('Primeiro Salto: '))
        segundoSalto = float(input('Segundo Salto: '))
        terceiroSalto = float(input('Terceiro Salto: '))
        quartoSalto = float(input('Quarto Salto: '))
        quintoSalto = float(input('Quinto Salto: '))

        somaSaltos = primeiroSalto + segundoSalto + \
            terceiroSalto + quartoSalto + quintoSalto
        if (primeiroSalto >= segundoSalto) and (primeiroSalto >= terceiroSalto) and (primeiroSalto >= quartoSalto) and \
           (primeiroSalto >= quintoSalto):
            melhorSalto = primeiroSalto
            
        elif (segundoSalto >= terceiroSalto) and (terceiroSalto >= quartoSalto) and (quartoSalto >= quintoSalto):
            melhorSalto = segundoSalto
            
        elif (terceiroSalto >= quartoSalto) and \
             (terceiroSalto >= quintoSalto):
            melhorSalto = terceiroSalto
            
        elif (quartoSalto >= quintoSalto):
            melhorSalto = quartoSalto
            
        else:
            melhorSalto = quintoSalto
        somaSaltos -= melhorSalto

        if (primeiroSalto <= segundoSalto) and (primeiroSalto <= terceiroSalto) and (primeiroSalto <= quartoSalto) and \
           (primeiroSalto <= quintoSalto):
            piorSalto = primeiroSalto
        elif (segundoSalto <= terceiroSalto) and (terceiroSalto <= quartoSalto) and (quartoSalto <= quintoSalto):
            piorSalto = segundoSalto
        elif (terceiroSalto <= quartoSalto) and (terceiroSalto <= quintoSalto):
            piorSalto = terceiroSalto
        elif (quartoSalto <= quintoSalto):
            piorSalto = quartoSalto
        else:
            piorSalto = quintoSalto
        somaSaltos -= piorSalto

        print('Melhor Salto: {:.2f}'.format(melhorSalto))
        print('Pior Salto: {:.2f} m'.format(piorSalto))
        print('Media dos demais saltos: {:.2f} m'.format(somaSaltos / 3.0))
        print('Resultado Final: {}: {:.0f} m'.format(nomeAtleta, (somaSaltos / 3.0)))