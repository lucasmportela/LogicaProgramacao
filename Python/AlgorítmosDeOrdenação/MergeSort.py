def merge_sort(lista):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas.
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas metades.
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    # Junta as duas metades ordenadas.
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0

    # Compara os elementos das duas listas.
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(lista))
