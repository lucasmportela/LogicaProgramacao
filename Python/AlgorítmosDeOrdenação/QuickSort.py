
def particionar(lista, inicio, fim):
    # Escolhe o último elemento como pivô
    pivo = lista[fim]

    # Índice do último elemento menor que o pivô
    i = inicio - 1

    # Percorre o trecho comparando cada item com o pivô
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1

            # Troca o item menor para o lado esquerdo
            lista[i], lista[j] = lista[j], lista[i]

    # Posiciona o pivô corretamente
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

    return i + 1


def quicksort_recursivo(lista, inicio, fim):
    if inicio < fim:
        # Encontra a posição correta do pivô
        indice_pivo = particionar(lista, inicio, fim)

        # Ordena a metade esquerda
        quicksort_recursivo(lista, inicio, indice_pivo - 1)

        # Ordena a metade direita
        quicksort_recursivo(lista, indice_pivo + 1, fim)


def quicksort(lista):
    # Inicia a ordenação da lista inteira
    quicksort_recursivo(lista, 0, len(lista) - 1)
    return lista


if __name__ == "__main__":
    lista = [0, 3, 1, 5, 19, 2, 55]
    print(quicksort(lista))
