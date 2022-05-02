'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos 
são obrigatórios.
'''

print("**********************************")
print('***CLASSE***CONTA***CORRENTE***!**')
print("**********************************")

class ContaCorrente():
    def __init__(self,numero,nome,saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        print(f'Nº Conta: {self.numero} | Nome: {self.nome} | Saldo: {self.saldo}')
        
    def AlterarNome(self,nome):
        self.nome = nome
        return self.nome
    
    def Deposito(self,valor):
            self.saldo += valor
            return self.saldo
    
    def Sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            print('Erro no Saque !')
            return self.saldo
    
    def MostrarSaldo(self):
        print(f'Saldo Atual: R$ {self.saldo:.2f}')
    
saldo = ContaCorrente(1010,'Fernando Soares')
print('Nome alterado: {}'.format(saldo.AlterarNome('Fernando Prado')))
print('Deposito: {}'.format(saldo.Deposito(1000)))
print('Sacar: {}'.format(saldo.Sacar(50)))
