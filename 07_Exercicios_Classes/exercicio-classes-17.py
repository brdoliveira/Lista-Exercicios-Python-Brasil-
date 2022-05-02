'''
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento
do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada
opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os
bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante,dê para cada bichinho um nivel inicial aleatório de fome e
tédio.
'''
import random

print("**********************************")
print('***CLASSE**BICHINHO**VIRTUAL**!***')
print("**********************************")

class BichinhoVirtual():
    def __init__(self, nome):
        self.setNome(nome)
        self.setFome(random.randint(0,10))
        self.setSaude(random.randint(0,10))
        self.setIdade(random.randint(0,10))
        print(f'Nome: {self.nome} | Fome: {self.fome} | Saude: {self.saude} | Idade: {self.idade} | Humor: {self.getHumor()}')  

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, saude):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude += self.saude * (quantidade / 100.0)

    def getHumor(self):
        return self.getFome() * self.getSaude()
    
    def __str__(self):
        return str(f'Nome: {self.nome} | Fome: {self.fome} | Saude: {self.saude} | Idade: {self.idade} | Humor: {self.getHumor()}')

bicho = BichinhoVirtual('Cleber Coelho')
bichinho = BichinhoVirtual('Macaquinho Bariloche')
print(f'Humor: {bicho.getHumor()}')
bicho.alimenta(30)
print(f'Humor: {bicho.getHumor()}')
bicho.brincar(20)
print(f'Humor: {bicho.getHumor()}')
print(bicho)