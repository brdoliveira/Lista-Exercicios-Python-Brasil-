'''
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário
em uma certa porcentagem.

Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
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
    
    def AumentarSalario(self, percentualAumento):
        self.salario += self.salario * ( percentualAumento / 100.0)

    def ObterValores(self):
        print(f'| Nome: {self.nome} | Salário mensal: R${self.salario:.2f} |')
        
funcionario = Funcionario('Antoine Doinel',15000)
funcionario.AumentarSalario(20)
print('Nome:     {}'.format(funcionario.getNome()))
print('Salario:  {:.2f}'.format(funcionario.getSalario()))