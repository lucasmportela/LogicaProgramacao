# Exercício 4 — Sistema de monitoramento de bateria
# Nível intermediário
# Uma empresa desenvolve equipamentos industriais que funcionam com baterias. Para evitar falhas, é necessário criar um sistema que monitore a carga das baterias e impeça valores inválidos.
# Regras da atividade
# 1. Crie uma classe chamada Bateria.
# 2. Construtor __init__:
# - Deve receber identificacao (exemplo: "Bateria-A").
# - Deve receber capacidade_maxima em mAh.
# - Deve receber carga_atual, com valor padrão zero.
# 3. Atributo capacidade_maxima:
# - Deve ser protegido (_capacidade_maxima).
# - Deve possuir @property.
# - Não pode ser alterado depois da criação do objeto.
# 4. Atributo carga_atual:
# - Deve ser protegido (_carga_atual).
# - Deve possuir @property e @carga_atual.setter.
# - Não pode aceitar valores negativos.
# - Não pode ultrapassar a capacidade máxima.
# 5. Propriedade porcentagem_carga:
# - Deve ser somente leitura.
# - Deve calcular automaticamente a porcentagem de carga da bateria.
# 6. Propriedade alerta_bateria_fraca:
# - Deve retornar True se a carga estiver abaixo de 20%.
# - Deve retornar False caso contrário.
# 7. Método carregar(mAh):
# 8. Método descarregar(mAh):
class Bateria:
    def __init__(self, identificacao, capacidade_maxima, carga_atual = 0):
        self.identificacao = identificacao
        if capacidade_maxima <= 0:
            raise ValueError("A capacidade máxima deve ser maior que zero!")
        self._capacidade_maxima = capacidade_maxima
        self.carga_atual = carga_atual
    @property
    def capacidade_maxima(self):
        return self._capacidade_maxima
    @property
    def carga_atual(self):
        return self._carga_atual
    @carga_atual.setter
    def carga_atual(self, carga_atual):
        if 0 <= carga_atual <= self.capacidade_maxima:
            self._carga_atual = carga_atual
        else:
            raise ValueError("O carga atual não pode ser negativo ou maior que a carga máxima!")
    @property
    def porcentagem_carga(self):
        return(self._carga_atual / self.capacidade_maxima) * 100
    @property
    def alerta_bateria_fraca(self):
        return (self.porcentagem_carga) < 20
    def carregar (self, carga):
        if carga > 0 and self._carga_atual + carga <= self.capacidade_maxima:
            self.carga_atual += carga
            return True
        return False
    def descarregar (self, carga):
        if carga > 0 and self._carga_atual >= carga:
            self.carga_atual -= carga
            return True
        return False
bateria1 = Bateria("Bateria-A", 5000, 2000)
print(f"Identificação: {bateria1.identificacao}")
print(f"Capacidade: {bateria1.capacidade_maxima} mAh")
print(f"Carga atual: {bateria1.carga_atual} mAh")
print(f"Porcentagem: {bateria1.porcentagem_carga:.2f}%")
print(f"Bateria fraca: {bateria1.alerta_bateria_fraca}")
if bateria1.carregar(1500):
    print("Bateria carregada com sucesso!")
else:
    print("Não foi possível carregar!")
if bateria1.descarregar(1000):
    print("Bateria descarregada com sucesso!")
else:
    print("Não foi possível descarregar!")
print(f"Carga final: {bateria1.carga_atual} mAh")
print(f"Porcentagem final: {bateria1.porcentagem_carga:.2f}%")
