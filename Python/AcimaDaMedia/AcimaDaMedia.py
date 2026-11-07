# Construa um programa onde o usuário digitará o nome e a média de dez
# alunos e o programa escreverá, na tela, o nome de todos com a média acima
# ou igual a seis.
Notas = []
Nomes = []
AcimaMedia = []
for i in range(10):
    Nome = str(input(f"Digite o seu nome aluno {i + 1}: "))
    Nomes.append(Nome)
    Nota = float(input(f"Digite a sua média: "))
    Notas.append(Nota)
    if Nota >= 6:
        AcimaMedia.append(Nome)
print(f"{AcimaMedia} estão acima ou na média!")
