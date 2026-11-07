class Venda:
    def __init__(self):
        self._faturamento_total = 0.0
        self._total = 0.0
        self._produto = 0.0
        self._parcelas = 0
    def get_faturamento_total(self):
        return self._faturamento_total
    def set_faturamento_total(self, novo_faturamento):
        self._faturamento_total = novo_faturamento
    def adicionar_produto(self, valor):
        if valor < 0:
            print('Digite um valor válido')
            return False
        self._total += valor
        return True
    def calcular_desconto(self):
        if self._total > 200:
            self._total = self._total * 0.9
        elif self._total > 100:
            self._total = self._total * 0.95
        return self._total
    def calcular_parcelas(self, parcelas):
        if parcelas < 1 or parcelas > 6:
            print('Quantidade de parcelas inválidas')
            return False
        self._parcelas = parcelas
        return True
    def exibir_parcelas(self):
        valor_parcela = self._total / self._parcelas
        for i in range(self._parcelas, 0, -1):
            print(f'{i}º parcela de {valor_parcela:.2f}')
    def finalizar_venda(self):
        self._faturamento_total += self._total
        self._total = 0.0
    def exibir_faturamento(self):
        print(f'Faturamento total de: {self._faturamento_total:.2f}')
venda = Venda()
cliente = 1
while cliente != 0:
    produto = 0.0
    while produto != -1:
        produto = float(input('Informe o valor do produto: '))
        if produto != -1:
            venda.adicionar_produto(produto)
    venda.calcular_desconto()
    parcelas = int(input('Quantas parcelas serão? (1 a 6) '))
    while venda.calcular_parcelas(parcelas) == False:
        parcelas = int(input('Quantas parcelas serão? (1 a 6) '))
    venda.exibir_parcelas()
    venda.finalizar_venda()
    cliente = int(input('Novo cliente? '))
venda.exibir_faturamento()
