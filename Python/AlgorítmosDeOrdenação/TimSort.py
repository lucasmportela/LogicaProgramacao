def insertion_sort(lista, inicio, fim):
    # Ordena um bloco usando Insertion Sort
    for i in range(inicio + 1, fim):
        valor = lista[i]
        j = i - 1
        while j >= inicio and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    i = 0
    j = 0
    k = inicio
    # Combina os dois blocos ordenados
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1
    # Copia os elementos restantes
    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1
def tim_sort(lista):
    tamanho = len(lista)
    tamanho_bloco = 4
    # Ordena pequenos blocos com Insertion Sort
    for inicio in range(0, tamanho, tamanho_bloco):
        fim = min(inicio + tamanho_bloco, tamanho)
        insertion_sort(lista, inicio, fim)
    # Combina os blocos usando Merge Sort
    tamanho_bloco = tamanho_bloco
    while tamanho_bloco < tamanho:
        for inicio in range(0, tamanho, 2 * tamanho_bloco):
            meio = min(inicio + tamanho_bloco, tamanho)
            fim = min(inicio + 2 * tamanho_bloco, tamanho)
            if meio < fim:
                merge(lista, inicio, meio, fim)
        tamanho_bloco *= 2
    return lista
lista = [35, 12, 43, 8, 51, 24, 19, 3, 17, 6]
print(tim_sort(lista))