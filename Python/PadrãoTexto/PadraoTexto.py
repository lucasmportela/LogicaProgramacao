# Crie uma função que coloque qualquer texto no seguinte padrão e o retorne:
# ◆ Tudo em minúscula.
# ◆ Sem espaços na frente ou atrás (começando e finalizando o texto).
# Atualize (ou crie uma nova) a função anterior para retornar se há um número
# dentro do texto.
texto = input("Digite um texto: ")
def padronizar(texto):
    return texto.lower().strip()
padrao = padronizar(texto)

def vernum(texto):
    return any(char.isdigit() for char in texto)
numero = vernum(texto)

print(padrao)
print(f"Há um número no texto: {numero}")
