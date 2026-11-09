def insertion_sort(lista):
    tamanho = len(lista)

    # Começa no índice 1, pois o índice 0 já é considerado ordenado sozinho.
    for i in range(1, tamanho):
        chave = lista[i]
        posicao = i - 1

        # Move os elementos maiores que a chave uma posição para a frente.
        while posicao >= 0 and lista[posicao] > chave:
            lista[posicao + 1] = lista[posicao]
            posicao -= 1

        # Insere a chave no espaço correto.
        lista[posicao + 1] = chave

    return lista


if __name__ == "__main__":
    lista = [0, 3, 1, 5, 19, 2, 55]
    print(insertion_sort(lista))
