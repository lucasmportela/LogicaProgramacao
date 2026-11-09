def bucket_sort(lista):
    if not lista:
        return []

    minimo = min(lista)
    maximo = max(lista)

    # Uma lista com valores iguais já está ordenada.
    if minimo == maximo:
        return lista.copy()

    quantidade = len(lista)
    baldes = [[] for _ in range(quantidade)]
    intervalo = maximo - minimo

    # Distribui os elementos proporcionalmente entre os baldes.
    for numero in lista:
        indice = int((numero - minimo) / intervalo * (quantidade - 1))
        baldes[indice].append(numero)

    # Ordena cada balde individualmente.
    for balde in baldes:
        balde.sort()

    # Junta os baldes em uma nova lista.
    resultado = []
    for balde in baldes:
        resultado.extend(balde)

    return resultado


if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6, 7]
    print(bucket_sort(lista))
