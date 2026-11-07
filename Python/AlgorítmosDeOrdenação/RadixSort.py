def counting_sort(lista, expoente):
    tamanho = len(lista)
    resultado = [0] * tamanho
    contagem = [0] * 10
    # Conta a frequência de cada dígito
    for numero in lista:
        digito = (numero // expoente) % 10
        contagem[digito] += 1
    # Calcula as posições acumuladas
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    # Constrói o resultado de trás para frente
    # para preservar a estabilidade da ordenação
    for i in range(tamanho - 1, -1, -1):
        digito = (lista[i] // expoente) % 10
        resultado[contagem[digito] - 1] = lista[i]
        contagem[digito] -= 1
    # Copia os valores ordenados para a lista original
    for i in range(tamanho):
        lista[i] = resultado[i]
def radix_sort(lista):
    if not lista:
        return lista
    # Esta implementação aceita apenas inteiros não negativos
    if any(numero < 0 for numero in lista):
        raise ValueError("Use apenas números inteiros não negativos.")
    maior = max(lista)
    expoente = 1
    # Ordena pelas unidades, dezenas, centenas...
    while maior // expoente > 0:
        counting_sort(lista, expoente)
        expoente *= 10
    return lista
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(lista))
