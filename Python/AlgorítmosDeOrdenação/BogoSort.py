import random
def bogo_sort(lista):
    tentativas = 0
    while lista != sorted(lista):
        random.shuffle(lista)
        tentativas += 1
    print("Número de tentativas:", tentativas)
    return lista
# Exemplo de uso
lista = [12, 3, 6, 2, 9, 21, 17]
print(bogo_sort(lista))
