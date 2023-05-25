from Fisica import Fisica
from Cidade import Cidade
from Pessoa import Pessoa
from Juridica import Juridica

c1 = Cidade(1,"POA")
c2 = Cidade(2,"Capão da Canoa")


p1=Pessoa("Maria","097654321", c1)
pf1 = Fisica("João", "123456", c2,"000.111.222-33")

#p1.imprimir()
#pf1.imprimir()

print(p1)
print("---------------------------------")
print(pf1)

