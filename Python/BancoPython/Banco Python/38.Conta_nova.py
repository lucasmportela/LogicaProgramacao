from banco import Conta

# criar uma "sub conta", ela tem tudo que conta tem e 
# mais alguma coisa

# em Java:
# public class ContaCorrente extends Conta

# em Python:
# class ContaCorrente(Conta)

class ContaCorrente(Conta):
    '''
    Subclasse que especializa a Conta
    '''
    # metodo construtor
    def __init__(self, titular, conta, saldo=0.0, taxa_saque=2.0):
        super().__init__(titular, conta, saldo)
        self._taxa_saque = taxa_saque

    # quero reescrever o metodo de saque
    # usar o mesmo método reescrito = Polimorfismo
    def realizar_saque(self, valor):
        if valor <= 0:
            print('Valor não válido')
            return False
        custo_total = valor + self._taxa_saque
        if self.get_saldo() < custo_total:
            print('Não há saldo suficiente')
            return False

        # caminho feliz
        novo_saldo = self.get_saldo() - custo_total
        self._extrato.append(f'Transação: Saque\nSaldo Anterior: R$ {self.get_saldo():.2f} -> Novo Saldo: R$ {novo_saldo:.2f}')
        self.set_saldo(novo_saldo)
        return True



teste = Conta('Homer', '0003', 50)
teste.realizar_saque(10)
teste.exibir_extrato()

print('\n' + '='*50 + '\n')

teste2 = ContaCorrente('Victor', '00004', 100)
teste2.realizar_saque(10)
teste2.exibir_extrato()