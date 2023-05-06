from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempoDaBateria=None):
        super().__init__(modelo, cor, preco)
        self.__tempoDaBateria = tempoDaBateria

    def getInformacoes(self):
        print("-------------------")
        super().imprimir()
   
    
    def get_Bat(self):
        return self.__tempoDaBateria
    
        
     
    def Cadastrar(self):
        print("*******************************")
        print ("Cadastro de Equipamento")
        print(" ")
        choice = str(input ("Deseja cadastrar o equipamento (s/n) ?").lower())
        print(" ")
        if choice == "s":
            print ("Notebook Cadastrado !")

        else:
            print("FIM")