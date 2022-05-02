'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

print("**********************************")
print('*******CLASSE***PESSOA***!********')
print("**********************************")

class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        print(f'Nome: {self.nome} | Idade: {self.idade} | Peso : {self.peso} | Altura: {self.altura}')
        
    def Envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05
            
        return self.idade , self.altura
    
    def Engordar(self,engordou):
        self.peso += engordou
        return self.peso

    def Emagrecer(self,emagreceu):
        self.peso -= emagreceu
        return self.peso
    
    def Crescer(self,cresceu):
        self.altura += cresceu
        return self.altura    
    
pessoinha = Pessoa('Fernando',19,60.0,1.75)
print(f'Peso (Engordar): {pessoinha.Engordar(5)}')
print(f'Peso (Emagrecer): {pessoinha.Emagrecer(10)}')
print(f'Altura (Crescer): {pessoinha.Crescer(0.05)}')
