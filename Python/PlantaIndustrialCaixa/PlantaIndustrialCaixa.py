# 3. Uma planta industrial precisa monitorar caixas d'água e reservatórios químicos para
# evitar transbordamento ou funcionamento de bombas a seco.
# i. Crie uma classe chamada Reservatorio que controle o nível de fluido de forma
# estritamente segura.
# ii. Na próxima página tem as restrições/passo-a-passo.
# i. O construtor deve receber a identificacao (ex: "Tanque-A"), a capacidade_maxima em
# litros e o nivel_inicial (padrão zero).
# ii. O atributo capacidade_maxima deve ser protegido e acessível apenas para leitura via
# @property (não deve ser alterado após a construção).
# iii. O atributo nivel_atual deve ser protegido (_nivel_atual) e possuir @property e
# @nivel_atual.setter. O setter deve garantir que o volume nunca fique abaixo de zero e
# nunca ultrapasse a capacidade_maxima.
# iv. Crie uma propriedade somente-leitura chamada porcentagem_ocupada que retorne o
# percentual atual de preenchimento do tanque (de 0 a 100%).
# v. Crie uma propriedade booleana alerta_nivel_baixo que retorne True se a ocupação
# estiver abaixo de 20%, e False caso contrário.
# vi. Implemente os métodos abastecer(litros) e consumir(litros) retornando True se a
# operação for concluída com sucesso ou False se a operação for rejeitada por limites
# físicos.
class Reservatorio:
    def __init__(self, identificacao, capacidade_maxima, nivel_inicial = 0):
        self.identificacao = identificacao
        self._capacidade_maxima = capacidade_maxima
        if capacidade_maxima <= 0:
            raise ValueError("A capacidade máxima deve ser maior que zero!")
        self.nivel_atual = nivel_inicial
    @property
    def capacidade_maxima(self):
        return self._capacidade_maxima
    @property
    def nivel_atual(self):
        return self._nivel_atual
    @nivel_atual.setter
    def nivel_atual(self, nivel_atual):
        if 0 <= nivel_atual <= self.capacidade_maxima:
            self._nivel_atual = nivel_atual
        else:
            raise ValueError("O nível não pode ser negativo ou ultrapassar a capacidade máxima!")
    @property
    def porcentagem_ocupada(self):
        return (self._nivel_atual / self.capacidade_maxima) * 100
    @property
    def alerta_nivel_baixo(self):
        return self.porcentagem_ocupada < 20
    def abastecer(self, litros):
        if litros > 0 and self._nivel_atual + litros <= self.capacidade_maxima:
            self.nivel_atual += litros
            return True
        return False
    def consumir(self, litros):
        if litros > 0 and self._nivel_atual >= litros:
            self.nivel_atual -= litros
            return True
        return False
reservatorio1 = Reservatorio("Tanque-A", 1000, 500)
print(f"Identificação: {reservatorio1.identificacao}")
print(f"Capacidade máxima: {reservatorio1.capacidade_maxima} litros")
print(f"Nível atual: {reservatorio1.nivel_atual} litros")
print(f"Porcentagem ocupada: {reservatorio1.porcentagem_ocupada:.2f}%")
print(f"Alerta de nível baixo: {reservatorio1.alerta_nivel_baixo}")
if reservatorio1.abastecer(300):
    print("Abastecimento realizado com sucesso!")
else:
    print("Não foi possível abastecer!")
if reservatorio1.consumir(200):
    print("Consumo realizado com sucesso!")
else:
    print("Não foi possível consumir!")
print(f"Nível final: {reservatorio1.nivel_atual} litros")
print(f"Ocupação final: {reservatorio1.porcentagem_ocupada:.2f}%")