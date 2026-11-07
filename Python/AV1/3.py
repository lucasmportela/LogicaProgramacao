# Construa um programa em Python que receba os dados para preencher uma matriz 3x3 com
# números inteiros informados pelo usuário. Após o preenchimento, o sistema deve solicitar um valor
# numérico de corte (limiar). O programa deve varrer a matriz, contabilizar quantos elementos são
# estritamente maiores que esse limiar e gerar uma segunda matriz 3x3 onde todos os valores
# superiores ao limiar sejam substituídos por 0, mantendo os demais inalterados. Ao final, exiba a
# contagem de elementos acima do limiar e a matriz resultante formatada em linhas e colunas.
Matriz = []
Limiar = 0
Contador = 0
for i in range (3):
    Linha = [] #cria a linha
    for j in range (3):
        Num = int(input(f"Digite o número { {i} }{ {j} } : "))
        Linha.append(Num) #insere os valores na linha
    Matriz.append(Linha) #insere a linha nas colunas
Limiar = int (input("Digite um valor numérico de corte: ")) #cria o valor de corte
for i in range (3):
    for j in range (3):
        if Matriz[i][j] > Limiar: #verifica se o valor é maior que o limiar
            Matriz[i][j] = 0 #se for ele altera para 0
            Contador += 1 #conta a quantidade de valores acima de 0
print(f"Números acima do limiar : {Contador}")
for Linha in Matriz: #exibe a matriz
    print(Linha)
