'''
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. 
Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. 
Dica: acrescente um método especial str() à classe Bichinho.
'''


print("**********************************")
print('***CLASSE**BICHINHO**VIRTUAL**!***')
print("**********************************")

class BichinhoVirtual():
    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)
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

bicho = BichinhoVirtual('Cleber Coelho', 10, 10, 10)
print(f'Humor: {bicho.getHumor()}')
bicho.alimenta(30)
print(f'Humor: {bicho.getHumor()}')
bicho.brincar(20)
print(f'Humor: {bicho.getHumor()}')
print(bicho)