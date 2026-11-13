# Crie uma classe chamada Usuario aplicando encapsulamento para proteger
# as credenciais de acesso:
# i. O construtor __init__ deve receber username e senha.
# ii. Armazene username como atributo público comum (self.username = username).
# iii. Proteja os atributos internos com underline: self._senha (iniciando vazia "") e
# self._tentativas_falhas (iniciando em 0).
# iv. Crie um @property para senha que não revele o texto original, retornando uma
# máscara de asteriscos do mesmo tamanho da senha armazenada ("*" *
# len(self._senha)).
# Crie um @senha.setter que aceite a alteração apenas se a nova senha tiver pelo
# menos 6 caracteres e não contiver espaços em branco. Caso contrário, exiba uma
# mensagem de erro e mantenha a senha anterior.
# vi. No __init__, atribua self.senha = senha (sem underline) para que a senha inicial já
# passe pelo verificador.
# vii. Crie uma propriedade somente-leitura chamada bloqueado (apenas @property, sem
# setter) que retorne True se self._tentativas_falhas >= 3, e False caso contrário.
# viii. Crie o método autenticar(senha_digitada):
# a. Se a conta já estiver bloqueada (self.bloqueado), exiba uma mensagem de
# bloqueio e retorne False.
# b. Se a senha_digitada for igual à self._senha, zere self._tentativas_falhas e retorne
# True.
# c. Se estiver incorreta, some 1 em self._tentativas_falhas e retorne False.
class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self._senha = senha
        self._tentativas_falhas = 0
        self.senha = senha
    @property
    def senha (self):
        return "*" * len(self._senha)
    @senha.setter
    def senha(self, nova_senha):
        if (isinstance(nova_senha, str)and len(nova_senha) >= 6 and not any(caractere.isspace() for caractere in nova_senha)):
            self._senha = nova_senha
        else:
            raise ValueError("Erro: a senha deve ter pelo menos 6 caracteres e não conter espaços!")
    @property
    def bloqueado(self):
        return self._tentativas_falhas >= 3
    def autenticar(self, senha_digitada):
        if (self.bloqueado == True):
            print("Bloqueado!")
            return False
        if (senha_digitada == self._senha):
            self._tentativas_falhas = 0
            return True
        else: 
            self.tentativas_falhas =+ 1
            return False
usuario = Usuario("lucas", "senha123")
print("Usuário:", usuario.username)
print("Senha:", usuario.senha)
print(usuario.autenticar("senhaerrada"))
print(usuario.autenticar("senhaerrada"))
print(usuario.autenticar("senhaerrada"))
print("Conta bloqueada?", usuario.bloqueado)