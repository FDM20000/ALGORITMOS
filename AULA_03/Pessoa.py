from Cidade import Cidade

class Pessoa:
        def __init__(self, name, fone, cidade):
            self.id = None
            self.nome = name
            self.fone = fone
            self.city = cidade

        def imprimir(self):
            print("Nome: ", self.nome)
            print("Telefone: ", self.fone)
            print("Cidade: ", self.city.nome )
