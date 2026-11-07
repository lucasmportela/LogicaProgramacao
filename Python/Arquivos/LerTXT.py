# Forma recomendada: iteracao direta e eficiente
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # .strip() remove espaços e quebra de linha \n
        print(linha.strip())