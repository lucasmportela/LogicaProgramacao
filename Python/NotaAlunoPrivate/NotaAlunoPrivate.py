# 1. Crie uma classe chamada Aluno para gerenciar a nota de um estudante de
# forma segura:
# i. O construtor __init__ deve receber o nome do aluno e a sua nota inicial.
# ii. Guarde o nome como atributo público comum (self.nome = nome).
# iii. Proteja o atributo da nota utilizando um underline (self._nota).
# iv. Crie um @property para permitir a leitura de nota.
# v. Crie um @nota.setter que só permita alterar a nota se o valor estiver entre 0.0 e
# 10.0. Caso contrário, exiba uma mensagem de erro e rejeite a alteração.
# vi. No construtor __init__, atribua self.nota = nota (sem underline) para forçar que a
# validação do setter já ocorra na hora de criar o objeto.
# vii. Crie uma propriedade somente-leitura chamada aprovado (apenas com
# @property, sem setter) que retorne True se a nota for maior ou igual a 6.0, e False
# caso contrário.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, valor):
        if 0.0 <= valor <= 10.0:
            self._nota = valor
        else:
            print("Erro: a nota deve estar entre 0.0 e 10.0!")
    @property
    def aprovado(self):
        return self._nota >= 6.0
aluno1 = Aluno("Lucas", 8.5)
print(f"Nome: {aluno1.nome}")
print(f"Nota: {aluno1.nota}")
print(f"Aprovado: {aluno1.aprovado}")
aluno1.nota = 5.0
print(f"Nova nota: {aluno1.nota}")
print(f"Aprovado: {aluno1.aprovado}")
aluno1.nota = 11.0
print(f"Nota após tentativa inválida: {aluno1.nota}")
