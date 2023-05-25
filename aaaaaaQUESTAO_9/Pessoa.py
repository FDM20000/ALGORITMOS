from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self,id=None, nome=None, telefone=None):
        self.id = id
        self.nome = nome
        self._telefone = telefone
        
    @abstractmethod
    def marcarPresenca(self):
        pass
    
    def matricular(self,matricula):
        self.__matricula = matricula
        
    # Método Acessor
    def getMatricula(self):
           return self.__matricula
        
    #Metodo Modificador
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
        self.__matricula
        
    
