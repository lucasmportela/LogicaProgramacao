class Node:
    def __init__(self, cod):
        self.cod = cod
        self.left = None
        self.right = None
def inserir(raiz, cod):
    if raiz is None:
        return Node(cod)
    if cod < raiz.cod:
        raiz.left = inserir(raiz.left, cod)
    elif cod > raiz.cod:
        raiz.right = inserir(raiz.right, cod)
    return raiz
def arvore_print(raiz, nivel=0, lado="Raiz"):
    if raiz is None:
        return
    print("    " * nivel + f"{lado}: {raiz.cod}")
    arvore_print(raiz.left, nivel + 1, "Esq")
    arvore_print(raiz.right, nivel + 1, "Dir")
def main():
    valores = [10, 15, 20, 12, 5]
    raiz = None
    for cod in valores:
        raiz = inserir(raiz, cod)
    print("=== Árvore Binária de Busca ===")
    arvore_print(raiz)
if __name__ == "__main__":
    main()
