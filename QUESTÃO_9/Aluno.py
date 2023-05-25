from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, telefone, presencas = 0):
        super().__init__(id, nome, telefone)
        self.presencas = presencas
        
    def marcarPresenca(self):
        chamada = str(input("Aluno presente ? (s/n)").lower())
        if chamada == "s":
            self.presencas = self.presencas + 1
        
        else:
            print("Aluno ausente !")
            
    
        
            
     