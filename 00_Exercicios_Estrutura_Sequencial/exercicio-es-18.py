'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

print("**********************************")
print("***TELECOM**DOS**TRABALHADORES****")
print("**********************************")

tamanho_arquivo = float(input("INSIRA TAMANHO DO ARQUIVO DESEJADO:  "))
velocidade = float(input("VELOCIDADE DO LINK DE INTERNET:  "))

tempo = tamanho_arquivo / velocidade

print('O tempo de download deste arquivo é de aproximadamente de {:.1f} minutos'.format(tempo))
