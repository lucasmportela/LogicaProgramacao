lista = [0,3,1,5,19,2,55]

def insertion_sort (lista):
    tamanho = len(lista)
    # Começa no índice 1, pois o índice 0 já é considerado ordenado sozinho
    for i in range(1, tamanho):
        chave = lista[i]
        posicao = i - 1
        # Move os elementos que são maiores que a chave uma posição para a frente 
        while posicao >= 0 and lista [posicao] > chave:
            lista[posicao + 1] = lista[posicao]
            posicao -= 1
    # Insere a chave no espaço correto liberado 
        lista[posicao + 1] = chave
    return lista

insertion_sort(lista)
print(lista)