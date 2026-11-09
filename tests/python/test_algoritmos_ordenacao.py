from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]

PASTA_ALGORITMOS = (
    ROOT / "Python" / "AlgorítmosDeOrdenação"
)


def carregar_modulo(nome, arquivo):
    caminho = PASTA_ALGORITMOS / arquivo

    spec = spec_from_file_location(nome, caminho)
    modulo = module_from_spec(spec)
    spec.loader.exec_module(modulo)

    return modulo


bubble_sort = carregar_modulo(
    "bubble_sort_module",
    "BubbleSort.py"
).bubble_sort

quicksort = carregar_modulo(
    "quicksort_module",
    "QuickSort.py"
).quicksort


@pytest.mark.parametrize(
    "algoritmo",
    [bubble_sort, quicksort],
    ids=["Bubble Sort", "Quick Sort"]
)
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ([], []),
        ([7], [7]),
        ([5, 2, 8, 1], [1, 2, 5, 8]),
        ([3, -1, 3, 0, -5], [-5, -1, 0, 3, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ]
)
def test_algoritmos_de_ordenacao(
    algoritmo,
    entrada,
    esperado
):
    resultado = algoritmo(entrada.copy())

    assert resultado == esperado