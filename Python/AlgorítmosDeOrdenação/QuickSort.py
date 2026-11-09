if __name__ == "__main__":
    def particionar (lista, inicio, fim):
        # Escolhe o último elemento como pivô
        pivo = lista[fim]
        # Índice do último elemento menor que o pivô encontrado
        i = inicio - 1
        # Percorre o trecho comparando cada item com o pivô 
        for j in range (inicio, fim): 
            if lista[j] <= pivo:
                i += 1
                # Troca o item menor para o lado esquerdo 
                lista[i], lista[j] = lista[j], lista[i]
        # Coloca o pivô logo após o último item menor que ele 
        lista[i+1], lista[fim] = lista [fim], lista[i+1]
        # Retorna o índice onde o pivô foi posicionado definitivamente 
        return i + 1

    def quicksort_recursivo (lista, inicio, fim):
        if inicio < fim:
            # Encontra a posição correta do pivô e separa a lista 
            indice_pivo = particionar (lista, inicio, fim)
            # Ordena a metade à esquerda do pivô quicksort_recursivo 
            quicksort_recursivo(lista, inicio, indice_pivo - 1)
            # Ordena a metade à direita do pivô quicksort_recursivo 
            quicksort_recursivo(lista, indice_pivo + 1, fim)

    def quicksort(lista):
        #Função principal que dispara a recursão cobrindo o vetor todo
        quicksort_recursivo(lista, 0, len(lista) - 1)
        return lista
    lista = [0, 3, 1, 5, 19, 2, 55]
    print(quicksort(lista))
if __name__ == "__main__":
    lista = [0, 3, 1, 5, 19, 2, 55]
    print(quicksort(lista))