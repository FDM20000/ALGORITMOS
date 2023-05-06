from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo=None, cor=None, preco=None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco
    
    @abstractmethod
    def Cadastrar(self):
        pass

    def imprimir(self):
        print ("Modelo: " + self.modelo)
        print ("Cor: " + self.cor)
        print ("Preço: R$ " + str(self.preco))

    @abstractmethod
    def PerTypePrint(self):
        pass


