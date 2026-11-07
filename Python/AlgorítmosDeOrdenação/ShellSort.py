def shell_sort(lista):
    tamanho = len(lista)
    intervalo = tamanho // 2
    # Reduz o intervalo a cada etapa
    while intervalo > 0:
        # Percorre a lista usando o intervalo atual
        for i in range(intervalo, tamanho):
            valor = lista[i]
            j = i
            # Compara elementos separados pelo intervalo
            while j >= intervalo and lista[j - intervalo] > valor:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = valor
        # Diminui o intervalo pela metade
        intervalo //= 2
    return lista
lista = [35, 12, 43, 8, 51, 24, 19, 3]
print(shell_sort(lista))