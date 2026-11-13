# Crie uma classe chamada CartaoAcesso aplicando encapsulamento para proteger o PIN de acesso de um usuário.
# i. O construtor __init__ deve receber titular e pin.
# ii. Armazene titular como atributo público comum (self.titular = titular).
# iii. Proteja os atributos internos utilizando underline:
# - self._pin (iniciando como string vazia "").
# - self._tentativas_invalidas (iniciando em 0).
# iv. Crie um @property para pin que não revele o PIN original, retornando uma máscara de asteriscos do mesmo tamanho do PIN armazenado.
# v. Crie um @pin.setter que aceite a alteração somente se o novo PIN:
# - Possuir exatamente 4 caracteres.
# - Contiver apenas números.
# - Caso contrário, exiba uma mensagem de erro e mantenha o PIN anterior.
# vi. No __init__, atribua self.pin = pin (sem underline), para que o PIN inicial também passe pela validação.
# vii. Crie uma propriedade somente leitura chamada bloqueado (apenas @property, sem setter), que retorne:
# - True se self._tentativas_invalidas >= 3.
# - False caso contrário.
# viii. Crie o método autenticar(pin_digitado):
# a. Se o cartão já estiver bloqueado (self.bloqueado), exiba uma mensagem informando o bloqueio e retorne False.
# b. Se o PIN digitado for igual ao PIN armazenado (self._pin), zere self._tentativas_invalidas e retorne True.
# c. Se o PIN estiver incorreto, incremente self._tentativas_invalidas em 1 e retorne False.
class CartaoAcesso:
    def __init__(self,titular, pin):
        self.titular = titular
        self._pin = ""
        self._tentativas_invalidas = 0
        self.pin = pin
    @property
    def pin (self):
        return "*" * len(self._pin)
    @pin.setter
    def pin (self, novo_pin):
        if len(novo_pin) == 4 and novo_pin.isdigit():
            self._pin = novo_pin
        else:
            print("O PIN deve conter 4 números")
    @property
    def bloqueado (self):
        if self._tentativas_invalidas >=3: 
            return True
        return False
    def autenticar(self, pin_digitado):
        if self.bloqueado == True:
            print ("Bloqueado!")
            return False
        if pin_digitado == self._pin:
            self._tentativas_invalidas = 0
            return True
        else:
            self._tentativas_invalidas += 1
            return False
