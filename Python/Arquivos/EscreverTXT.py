# f = open("dados.txt", "w")
# f.write("teste")
# f.close() Se der erro na linha anterior, isso nunca executa
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("ABCD\n")
    arquivo.write("Segunda linha.\n")
# Fechado automaticamente ao sair da indentação
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Nova linha\n")
    # Adicioa uma nova linha no txt