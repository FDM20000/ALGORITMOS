from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempoDaBateria=None):
        super().__init__(modelo, cor, preco)
        self.__tempoDaBateria = tempoDaBateria

    def getInformacoes(self):
        print("-------------------")
        super().imprimir()
   
    def PerTypePrint(self):
        print("Tempo da Bateria (hs): " +str(self.__tempoDaBateria))
        
     
    def Cadastrar(self):
        print("*******************************")
        print ("Cadastro de Equipamento")
        print(" ")
        choice = str(input ("Deseja cadastrar o equipamento (s/n) ?").lower())
        if choice == "s":
            print ("Notebook Cadastrado !")
        else:
            print("FIM")