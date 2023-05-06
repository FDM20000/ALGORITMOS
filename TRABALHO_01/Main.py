from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

comp = None

print("""Executar para Desktop ou Notebook ?

1 = Desktop
2 = Notebook 
""")
comp = input("Digite sua escolha: ")
print("------------------------------")

if comp == "1":
    desk = Desktop("TK2000", "Preto", 1000, 200)
    print("DESKTOP")
    desk.imprimir()
    desk.PerTypePrint()
    desk.Cadastrar()
    print("=====================")

else:
    note = Notebook("Aspire F15", "Blue", 3000, 2)
    print("NOTEBOOK")
    note.imprimir()
    bateria = str(note.get_Bat())
    print("Tempo da Bateria (hs): " +(bateria))  
    note.Cadastrar()
    print("++++++++++++++++++++++")

