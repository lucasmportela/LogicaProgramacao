
def bubble_sort(lista):
    tamanho = len(lista)
    # Laço externo: controla quantas passadas serão feitas
    for i in range(tamanho):
        houve_troca = False
        # Laço interno: compara os pares vizinhos
        # Conforme 'i' cresce, os últimos elementos já estão nas posições corretas
        for  j in range(0 , tamanho - i - 1):
            if lista[j] > lista[j+1]:
            # Faz a troca direta de valores entre posições vizinhas 
                lista[j], lista[j+1] = lista[j+1], lista[j]
                houve_troca = True
            # Se nenhuma troca ocorreu nesta passada, a lista já está ordenada
        if not houve_troca:
            break
    return lista
    bubble_sort(lista)
    print(lista)
if __name__ == "__main__":
    lista = [0, 3, 1, 5, 19, 2, 55]
    print(bubble_sort(lista))