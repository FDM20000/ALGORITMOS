from Computador import Computador

n=0
class Desktop(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, potenciaDaFonte=None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        super().imprimir()
    
    def PerTypePrint(self):
        print("Potência da Fonte (W): " +str(self._potenciaDaFonte))
  

    def Cadastrar(self):
        print("*******************************")
        print ("Cadastro de Equipamento")
        print(" ")
        choice = str(input ("Deseja cadastrar o equipamento (s/n) ?").lower())
        print(" ")
        if choice == "s":
            print ("Desktop Cadastrado !")
        
        else:
            print("FIM")

