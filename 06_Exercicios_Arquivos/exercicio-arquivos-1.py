'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos 
endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

print("**********************************")
print('***VALIDA**OU**INVALIDA**IP***!***')
print("**********************************")

def valido_ip(endereco_ip):
    blocos = endereco_ip.split('.')
    if (len(blocos) != 4):
        return False
    for i in blocos:
        i_i = int(i)
        if (i_i < 0) or (i_i > 255):
            return False
    return True

arquivo_entrada = open('1-entrada.txt', 'r')
linhas = arquivo_entrada.readlines()
arquivo_entrada.close()

ips_validos = []
ips_invalidos = []

for ip in linhas:
    if (valido_ip(ip.strip())):
        ips_validos.append(ip.strip())
    else:
        ips_invalidos.append(ip.strip())

arquivo_saido = open('1-saida.txt', 'w')

arquivo_saido.write('[IPs Validos]\n')
for ip in ips_validos:
    arquivo_saido.write('%s\n' % ip)

arquivo_saido.write('\n[IPs Invalidos]\n')
for ip in ips_invalidos:
    arquivo_saido.write('%s\n' % ip)

arquivo_saido.close()