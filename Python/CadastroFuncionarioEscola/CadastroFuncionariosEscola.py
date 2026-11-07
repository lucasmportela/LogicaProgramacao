# Construa um programa cadastrando cinco funcionários de uma escola,
# sendo que dois deles são professores.
# Todos os funcionários terão cadastrados seus nomes e salários.
# Os professores terão cadastrada também a disciplina que lecionam.
class Funcionarios:
    def __init__(self, nome, salario, cargo, disciplina):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.disciplina = disciplina
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        if self.disciplina == "Matemática":
            print(f"{self.nome} leciona Matemática!")
        if self.salario >= 2000:
            print("Salário acima de 2000!")
funcionarios = []
for i in range(5):
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salário: "))
    cargo = input("Digite seu cargo: ").strip().lower()
    disciplina = ""
    if cargo == "professor":
        disciplina = input("Digite sua disciplina: ").strip()
    funcionario = Funcionarios(nome, salario, cargo, disciplina)
    funcionarios.append(funcionario)
for funcionario in funcionarios:
    funcionario.mostrar_dados()