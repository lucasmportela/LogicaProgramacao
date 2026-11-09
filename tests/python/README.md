# Testes automatizados de Python

Esta pasta reúne os testes automatizados dos algoritmos de ordenação do repositório. A suíte utiliza **pytest** e é executada pelo GitHub Actions.

## Arquivos

| Arquivo | Responsabilidade |
|---|---|
| [`test_algoritmos_ordenacao.py`](test_algoritmos_ordenacao.py) | Testa resultados, casos-limite, tipos de entrada e preservação dos dados dos algoritmos de ordenação. |

## Cobertura atual

A suíte contém atualmente **102 casos de teste**, distribuídos da seguinte forma:

| Grupo de testes | Casos | O que verifica |
|---|---:|---|
| Casos comuns | 63 | Sete cenários para cada um dos nove algoritmos: lista vazia, um elemento, ordem aleatória, repetidos, ordenada, inversa e valores com diferentes quantidades de dígitos. |
| Números negativos | 24 | Três cenários para cada um dos oito algoritmos compatíveis com valores negativos. Radix Sort não participa deste grupo. |
| Bucket Sort com decimais e negativos | 1 | Ordenação de valores decimais positivos e negativos. |
| Validação do Radix Sort | 3 | Rejeição de números negativos, decimais e booleanos. |
| Preservação dos elementos | 9 | Confirma que cada algoritmo mantém a quantidade e os valores da entrada. |
| Imutabilidade do Merge Sort e Bucket Sort | 2 | Confirma que esses algoritmos retornam uma nova lista sem modificar a lista original. |
| **Total atual** | **102** | **Cobertura dos nove algoritmos.** |

### Algoritmos cobertos

- Bubble Sort
- Quick Sort
- Insertion Sort
- Merge Sort
- Heap Sort
- Radix Sort
- Bucket Sort
- Shell Sort
- Tim Sort

### Regras específicas verificadas

- **Radix Sort:** aceita apenas números inteiros não negativos. Entradas com números negativos geram `ValueError`; tipos diferentes de inteiro, incluindo `float` e `bool`, geram `TypeError`.
- **Bucket Sort:** é testado com números inteiros, decimais e negativos.
- **Merge Sort e Bucket Sort:** devem preservar a lista original e retornar uma lista ordenada independente.

## Como executar

Execute os comandos a partir da raiz do repositório:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/python -v
```

Para executar somente este arquivo de testes:

```bash
python -m pytest tests/python/test_algoritmos_ordenacao.py -v
```

Para verificar a sintaxe de todos os arquivos Python do repositório:

```bash
python -m compileall -q .
```

## Integração contínua

O workflow [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) executa:

1. Checkout do repositório.
2. Configuração do Python 3.12.
3. Verificação de sintaxe com `compileall`.
4. Instalação das dependências de desenvolvimento.
5. Execução dos testes com `pytest`.

A integração contínua é acionada em pushes e pull requests direcionados à branch `main`, além de permitir execução manual pelo GitHub Actions.

## Como manter esta documentação atualizada

Sempre que adicionar, remover ou alterar testes:

1. Execute a suíte completa com `python -m pytest tests/python -v`.
2. Confira o total de casos coletados e aprovados no resumo do pytest.
3. Atualize a tabela **Cobertura atual**, incluindo ou removendo os cenários correspondentes.
4. Atualize o total de casos neste arquivo, no [README principal](../../README.md) e no [README de Python](../../Python/README.md).
5. Confira se os comandos e as regras específicas continuam de acordo com o código e os testes.
6. Verifique se o GitHub Actions concluiu com sucesso.

> O número de testes documentado é uma fotografia da suíte no momento desta atualização. Sempre confirme o total no pytest antes de alterar esse número; não o estime apenas pela quantidade de funções de teste, pois testes parametrizados geram vários casos.
