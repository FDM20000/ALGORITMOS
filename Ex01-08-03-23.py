Refri = [("Coca",8.50,100),("Pepsi",7.90,100),("Fanta",8.00,100)]
Horti = [("Cebola",6.00,50),("Batata",7.50,50),("Cenoura",9.00,50)]
Cereais = [("Arroz",8.00,100),("Feijao",9.00,200),("Milho",12.00,100)]
Lista =[]

def Imprimir(pos):
    for i in Lista:
        if i == Lista[pos]:
            print(i)

def Excluir(pos):
    for i in Lista:
        if i == Lista[pos]:
            del(Lista[pos])
            print("Nova Lista:",Lista)

print("OPÇÕES:")
print("1 - Refrigerantes")
print("2 - Hortifrutigrangeiros")
print("3 - Cereais")

escolha = int(input("Escolha a Lista:"))

if escolha == 1:
    Lista = Refri
    print(Lista)
elif escolha == 2:
    Lista = Horti
else:
    Lista = Cereais
print("")
acao = input("Vc deseja IMPRIMIR PRODUTO DIGITE(I) ou EXCLUIR DIGITE(E) ?:").upper()
print("")

if acao == "I":
    for ele in enumerate(Lista):
        print(ele)
    pos = int(input("Qual posição do produto a imprimir ?"))
    Imprimir(pos)
else:
    for ele in enumerate(Lista):
        print(ele)
    pos = int(input("Qual posição do produto a excluir ?"))
    Excluir(pos)
