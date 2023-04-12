from Fisica import Fisica
from Cidade import Cidade
#from Pessoa import Pessoa
from Juridica import Juridica

c1 = Cidade(1,"POA")
c2 = Cidade(2,"Capão da Canoa")

joao = Fisica("João", "3322-4455", c1, "000.111.222-33")
maria = Fisica("Maria", "3344-5566",c2,"111.222.33-44")
jose = Fisica("Jose","3377-8899",c2,"444.555.666-99")

dosul = Juridica("Supermercado Do Sul", "265-4321", c2, "00.111.222/0001-02" )

dosul.addFuncionario(joao)
dosul.addFuncionario(maria)
dosul.addFuncionario(jose)
dosul.imprimir()

