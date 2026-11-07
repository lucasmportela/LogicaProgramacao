class Conta:

    # _  -> protected
    # __ -> private

    def __init__(self, nome, conta, saldo=0.0):
        self._nome = nome
        # essa variavel _nome é de fato _nome
        self._conta = conta
        # isso privado -> _Conta__conta
        self._saldo = saldo
        self._extrato = []

        # se a conta foi aberta com alguma quantia
        if self._saldo > 0:
            self._extrato.append(f'Depósito inicial: +R$ {self._saldo:.2f}')


    def get_saldo(self):
        # a ideia é não usar -> variavel._saldo
        # a ideia é chamar -> variavel.get_saldo()
        return self._saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo > 0:
            self._saldo = novo_saldo
        else:
            print('Novo saldo deve ser positivo')

    # ========================================================
    # ----------------- Forma Pythones -----------------------
    # ========================================================
    # GET
    @property
    def saldo(self):
        return self._saldo
    
    # SET
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo > 0:
            self._saldo = novo_saldo
        else:
            print('Novo saldo deve ser positivo')
    
    # ========================================================

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        if len(novo_nome) >= 3:
            self._nome = novo_nome
        else:
            print('Digite um nome com 3 ou mais caracteres')

    def get_conta(self):
        return self._conta

    # SEM SET_CONTA pelo fato que o numero da conta não deve ser mudado

    def realizar_deposito(self, valor):
        # verifica se o valor é positivo, entra caso não seja
        if valor <= 0:
            print('Digite um valor válido')
            return False

        # self._saldo += valor # ANTES
        novo_saldo = self.get_saldo() + valor
        self._extrato.append(f'Transação: Depósito\nSaldo Anterior: R$ {self.get_saldo():.2f} -> Novo Saldo: R$ {novo_saldo:.2f}')
        self.set_saldo(novo_saldo)
        return True

    def realizar_saque(self, valor):
        if valor <= 0:
            print('Digite um valor válido')
            return False
        if self.saldo < valor:
            print('Você não tem saldo suficiente')
            return False

        # caso tudo de certo, faz o saque
        # self.saldo = self.saldo - valor
        novo_saldo = self.get_saldo() - valor
        self._extrato.append(f'Transação: Saque\nSaldo Anterior: R$ {self.get_saldo():.2f} -> Novo Saldo: R$ {novo_saldo:.2f}')
        self.set_saldo(novo_saldo)
        return True

    def realizar_transferencia(self, conta_destino, valor):
        self._extrato.append(f'Iniciando a Transferência para {conta_destino.get_nome()} com o valor de R${valor:.2f}')
        
        if self.realizar_saque(valor) == True:
            self._extrato.append('Transferência finalizada com sucesso')
            # aqui é para quem esta recebendo
            conta_destino._extrato.append(f'Transferência recebida de {self.get_nome()} no valor de R$ {valor:.2f}')
            conta_destino.realizar_deposito(valor)
            conta_destino._extrato.append('Transferência finalizada com sucesso')
            return True
        else:
            self._extrato.append('Erro ao tentar realizar a Transferencia')
            return False

    def exibir_extrato(self):
        print('\n' + '='*45)
        print(f'Extrato - Conta: {self.get_conta()} - {self.get_nome()}')
        print('='*45)

        if not self._extrato:
            print('Não há transações nesta conta.')

        else:
            for transacao in self._extrato:
                print(f' - {transacao}')

        print('-'*45)
        print(f'Saldo consolidado: R$ {self.get_saldo():.2f}')
        print('='*45 + '\n')

# class ContaCorrente(Conta):
#     pass



# conta_do_Valim = Conta('Valim', '00001', 20)
# print(conta_do_Valim.get_saldo())
# print(conta_do_Valim.get_nome())
# conta_do_Valim.realizar_deposito(20)
# print(f'Saldo pós depósito: {conta_do_Valim.get_saldo()}')


# # conta_do_Valim.set_saldo(50)


# conta_do_Valim.realizar_saque(10)
# print(f'Saldo pós saque: {conta_do_Valim.get_saldo()}')

# conta_do_Maurilio = Conta('MauMau', '00002', 20)

# conta_do_Valim.realizar_transferencia(conta_do_Maurilio, 5)
# print(f'Pós Transferencia V: {conta_do_Valim.get_saldo()}')
# print(f'Pós Transferencia M: {conta_do_Maurilio.get_saldo()}')

# conta_do_Valim.exibir_extrato()