class Conta:

    # _  -> protected
    # __ -> private

    def __init__(self, nome, conta, saldo=0):
        self._nome = nome
        # essa variavel _nome é de fato _nome
        self._conta = conta
        # isso privado -> Conta__conta
        self._saldo = saldo

    def get_saldo(self):
        # a ideia é não usar -> variavel._saldo
        # a ideia é chamar -> variavel.get_saldo()
        return self._saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo > 0:
            self._saldo = novo_saldo
        else:
            print('Novo saldo deve ser positivo')

    # conta1._saldo = -10
    # conta1.set_saldo(-10)

    def realizar_deposito(self, valor):
        # verifica se o valor é positivo, entra caso não seja
        if valor <= 0:
            print('Digite um valor válido')
            return False

        self.saldo += valor
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
        self.saldo -= valor
        return True

    def realizar_transferencia(self, conta_destino, valor):
        if self.realizar_saque(valor) == True:
            conta_destino.realizar_deposito(valor)
            return True
        else:
            print('Transferencia Não Foi Realizada')
            return False

conta_do_Valim = Conta('Valim', '00001', 20)
print(conta_do_Valim.saldo)
print(conta_do_Valim.nome)
conta_do_Valim.realizar_deposito(20)
print(f'Saldo pós depósito: {conta_do_Valim.saldo}')

conta_do_Valim.realizar_saque(10)
print(f'Saldo pós saque: {conta_do_Valim.saldo}')

conta_do_Maurilio = Conta('MauMau', '00002', 20)

conta_do_Valim.realizar_transferencia(conta_do_Maurilio, 5)
print(f'Pós Transferencia V: {conta_do_Valim.saldo}')
print(f'Pós Transferencia M: {conta_do_Maurilio.saldo}')

# class Carro:

#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano


# c1 = Carro('Fiat', 'Palio', '2002')

# c2 = Carro('Ford', 'Fusion', '2014')

# c1[0] # marca
# c1[1] # modelo
# c1[2] # ano
# c1['marca'] = 'Fiat'
# c1['modelo'] = 'Palio'
# c1['ano'] = '2002'





# class Cachorro():

#     def __init__(self, raca, nome, genero, idade, pelagem):
#         self.raca = raca
#         self.nome = nome
#         self.genero = genero
#         self.idade = idade
#         self.pelagem = pelagem

#     def latir(self):
#         print('Au Au')
    
# dog1 = Cachorro('vira-lata', 'caramelo', 'neutro', 7, 'curto')

# dog1.latir()
# print(dog1.nome)



