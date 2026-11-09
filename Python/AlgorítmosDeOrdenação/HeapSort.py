def heap_sort(lista):
    tamanho = len(lista)

    # Organiza a lista em um Max Heap.
    def heapify(n, i):
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        # Verifica se o filho esquerdo é maior.
        if esquerda < n and lista[esquerda] > lista[maior]:
            maior = esquerda

        # Verifica se o filho direito é maior.
        if direita < n and lista[direita] > lista[maior]:
            maior = direita

        # Se um filho for maior, troca os elementos.
        if maior != i:
            lista[i], lista[maior] = lista[maior], lista[i]
            heapify(n, maior)

    # Constrói o Max Heap.
    for i in range(tamanho // 2 - 1, -1, -1):
        heapify(tamanho, i)

    # Move o maior elemento para o final da lista.
    for i in range(tamanho - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(i, 0)

    return lista


if __name__ == "__main__":
    lista = [1, 9, 7, 15, 21, 6]
    print(heap_sort(lista))
