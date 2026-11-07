# 2. Um sistema de faturamento comercial não pode permitir inconsistências cadastrais,
# como produtos com precos zerados/negativos ou estoques com quantidades abaixo de
# zero.
# i. Desenvolva uma classe chamada Produto que aplique encapsulamento para
# proteger essas regras de negócio.
# ii. Na próxima página tem as restrições/passo-a-passo.
# i. A classe deve inicializar com nome, preco e quantidade (padrão zero).
# ii. O atributo preco deve ser protegido (_preco) e controlado via @property e
# @preco.setter. O setter não deve aceitar valores menores ou iguais a zero.
# iii. O atributo quantidade deve ser protegido (_quantidade) e controlado via @property e
# @quantidade.setter. O setter não deve aceitar valores negativos.
# iv. O construtor __init__ deve obrigatoriamente acionar as propriedades (sem underline)
# para que os dados já nasçam validados na criação do objeto.
# v. Implemente a propriedade somente-leitura valor_total_estoque (apenas @property,
# sem setter), que calcula e retorna dinamicamente preco * quantidade.
# vi. Crie os métodos adicionar_estoque(quantidade) e remover_estoque(quantidade).
# a. O método de remoção deve validar se há saldo suficiente antes de subtrair,
# retornando um booleano de confirmação.
class Produto:
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, preco):
        if preco > 0:
            self._preco = preco
        else:
            raise ValueError("Preço tem que ser maior que zero!")
    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade >= 0:
            self._quantidade = quantidade
        else:
            raise ValueError("A quantidade não pode ser negativa!")
    @property
    def valor_total_estoque(self):
        return self._quantidade * self._preco
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            return True
        return False
    def remover_estoque(self, quantidade):
        if quantidade > 0 and self.quantidade >= quantidade:
            self.quantidade -= quantidade
            return True
        return False
produto1 = Produto("Notebook", 3500.00, 10)
print(f"Produto: {produto1.nome}")
print(f"Preço: R$ {produto1.preco:.2f}")
print(f"Quantidade: {produto1.quantidade}")
print(f"Valor total do estoque: R$ {produto1.valor_total_estoque:.2f}")
produto1.adicionar_estoque(5)
print(f"Estoque após adicionar: {produto1.quantidade}")
if produto1.remover_estoque(3):
    print("Estoque removido com sucesso!")
else:
    print("Não foi possível remover o estoque!")

print(f"Estoque final: {produto1.quantidade}")
print(f"Valor final do estoque: R$ {produto1.valor_total_estoque:.2f}")
