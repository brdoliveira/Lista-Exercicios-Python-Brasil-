'''
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se 
adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
'''

print("***********************************")
print('**CLASSE**CONTA**DE**INVESTIMENTO**')
print("***********************************")

class ContaInvestimento(object):
    def __init__(self, numero, nome, juros, saldo = 0.0):
        self.numero = numero
        self.nome = nome
        self.juros = juros
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.juros / 100.0))

conta = ContaInvestimento(1000, 'João Doria Trabalhador', 100)
conta.deposito(1000000)
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)