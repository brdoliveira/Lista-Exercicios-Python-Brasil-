'''
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
Escreva um pequeno programa que teste sua classe.
'''

print("**********************************")
print('*****CLASSE***FUNCIONÁRIO***!*****')
print("**********************************")

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)
        self.ObterValores()
        
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario

    def ObterValores(self):
        print(f'| Nome: {self.nome} | Salário mensal: R${self.salario:.2f} |')
        
funcionario = Funcionario('Antoine Doinel',15000)
print('Nome:     {}'.format(funcionario.getNome()))
print('Salario:  {:.2f}'.format(funcionario.getSalario()))
        