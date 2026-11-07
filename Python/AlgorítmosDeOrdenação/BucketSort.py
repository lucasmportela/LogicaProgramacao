def bucket_sort(lista):
    if len(lista) == 0:
        return lista
    # Cria os baldes
    quantidade = len(lista)
    baldes = [[] for _ in range(quantidade)]
    # Distribui os elementos nos baldes
    for numero in lista:
        indice = int(numero * quantidade)
        if indice >= quantidade:
            indice = quantidade - 1
        baldes[indice].append(numero)
    # Ordena cada balde individualmente
    for balde in baldes:
        balde.sort()
    # Junta os baldes em uma única lista
    resultado = []
    for balde in baldes:
        resultado.extend(balde)
    return resultado
lista = [12, 11, 13, 5, 6, 7]
print(bucket_sort(lista))