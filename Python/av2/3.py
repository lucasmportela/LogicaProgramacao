
# Criando a classe Livro
class Livro:

    # Construtor da classe
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):

        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    # Método para emprestar o livro
    def emprestar(self):

        if self.disponivel:

            self.disponivel = False

            print(f"Livro '{self.titulo}' emprestado com sucesso!")

        else:

            print(f"Aviso: O livro '{self.titulo}' já está emprestado.")

    # Método para devolver o livro
    def devolver(self):

        if not self.disponivel:

            self.disponivel = True

            print(f"Livro '{self.titulo}' devolvido com sucesso!")

        else:

            print(f"Aviso: O livro '{self.titulo}' já está disponível.")

    # Método para exibir a ficha técnica
    def exibir_ficha_tecnica(self):

        if self.disponivel:
            situacao = "Disponível"
        else:
            situacao = "Emprestado"

        print("\n========== FICHA TÉCNICA ==========")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_publicacao}")
        print(f"Situação: {situacao}")
        print("=" * 35)


# Criando dois objetos da classe Livro
livro1 = Livro("Python para Iniciantes", "Ana Souza", 2022)

livro2 = Livro("Clean Code", "Robert C. Martin", 2008)


# Exibindo as fichas iniciais
print("\n========== FICHAS INICIAIS ==========")

livro1.exibir_ficha_tecnica()
livro2.exibir_ficha_tecnica()


# Emprestando o livro 1
print("\n========== TESTE DE EMPRÉSTIMO ==========")

livro1.emprestar()


# Tentando emprestar novamente o livro 1
livro1.emprestar()


# Devolvendo o livro 1
print("\n========== TESTE DE DEVOLUÇÃO ==========")

livro1.devolver()


# Exibindo as fichas finais
print("\n========== FICHAS FINAIS ==========")

livro1.exibir_ficha_tecnica()
livro2.exibir_ficha_tecnica()
