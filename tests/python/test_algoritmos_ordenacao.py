from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
PASTA_ALGORITMOS = ROOT / "Python" / "AlgorítmosDeOrdenação"


def carregar_algoritmo(nome_modulo, arquivo, nome_funcao):
    caminho = PASTA_ALGORITMOS / arquivo
    spec = spec_from_file_location(nome_modulo, caminho)

    if spec is None or spec.loader is None:
        raise ImportError(f"Não foi possível carregar o módulo: {caminho}")

    modulo = module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return getattr(modulo, nome_funcao)


ALGORITMOS = [
    pytest.param(
        carregar_algoritmo("bubble_sort_module", "BubbleSort.py", "bubble_sort"),
        id="Bubble Sort",
    ),
    pytest.param(
        carregar_algoritmo("quicksort_module", "QuickSort.py", "quicksort"),
        id="Quick Sort",
    ),
    pytest.param(
        carregar_algoritmo("insertion_sort_module", "InsertionSort.py", "insertion_sort"),
        id="Insertion Sort",
    ),
    pytest.param(
        carregar_algoritmo("merge_sort_module", "MergeSort.py", "merge_sort"),
        id="Merge Sort",
    ),
    pytest.param(
        carregar_algoritmo("heap_sort_module", "HeapSort.py", "heap_sort"),
        id="Heap Sort",
    ),
    pytest.param(
        carregar_algoritmo("radix_sort_module", "RadixSort.py", "radix_sort"),
        id="Radix Sort",
    ),
    pytest.param(
        carregar_algoritmo("bucket_sort_module", "BucketSort.py", "bucket_sort"),
        id="Bucket Sort",
    ),
    pytest.param(
        carregar_algoritmo("shell_sort_module", "ShellSort.py", "shell_sort"),
        id="Shell Sort",
    ),
    pytest.param(
        carregar_algoritmo("tim_sort_module", "TimSort.py", "tim_sort"),
        id="Tim Sort",
    ),
]

ALGORITMOS_COM_NEGATIVOS = ALGORITMOS[:5] + ALGORITMOS[6:]

CASOS_COMUNS = [
    pytest.param([], id="lista vazia"),
    pytest.param([7], id="um elemento"),
    pytest.param([5, 2, 8, 1], id="ordem aleatoria"),
    pytest.param([3, 3, 0, 5, 3, 0], id="elementos repetidos"),
    pytest.param([1, 2, 3, 4, 5], id="ja ordenada"),
    pytest.param([9, 7, 5, 3, 1], id="ordem inversa"),
    pytest.param([0, 1000, 10, 1, 100], id="valores com diferentes digitos"),
]


@pytest.mark.parametrize("algoritmo", ALGORITMOS)
@pytest.mark.parametrize("entrada", CASOS_COMUNS)
def test_algoritmos_ordenam_casos_comuns(algoritmo, entrada):
    lista = entrada.copy()

    resultado = algoritmo(lista)

    assert resultado == sorted(entrada)
    assert sorted(resultado) == sorted(entrada)


@pytest.mark.parametrize("algoritmo", ALGORITMOS_COM_NEGATIVOS)
@pytest.mark.parametrize(
    "entrada",
    [
        pytest.param([-5, -1, -9, -3], id="todos negativos"),
        pytest.param([3, -1, 0, -5, 2], id="positivos e negativos"),
        pytest.param([-2, -2, 0, 2, 2], id="negativos e repetidos"),
    ],
)
def test_algoritmos_que_suportam_negativos(algoritmo, entrada):
    assert algoritmo(entrada.copy()) == sorted(entrada)


def test_bucket_sort_aceita_numeros_decimais_e_negativos():
    entrada = [-2.5, 1.2, 0.0, -1.1, 3.4, 1.2]

    assert carregar_algoritmo(
        "bucket_sort_float_module", "BucketSort.py", "bucket_sort"
    )(entrada.copy()) == sorted(entrada)


@pytest.mark.parametrize(
    "entrada",
    [
        pytest.param([-1, 0, 5], id="numero negativo"),
        pytest.param([1, 2.5, 3], id="numero decimal"),
        pytest.param([True, 0, 1], id="valor booleano"),
    ],
)
def test_radix_sort_rejeita_entradas_fora_do_contrato(entrada):
    radix_sort = carregar_algoritmo(
        "radix_sort_validation_module", "RadixSort.py", "radix_sort"
    )

    if any(type(numero) is not int for numero in entrada):
        with pytest.raises(TypeError, match="inteiros"):
            radix_sort(entrada.copy())
    else:
        with pytest.raises(ValueError, match="não negativos"):
            radix_sort(entrada.copy())


@pytest.mark.parametrize(
    "algoritmo",
    ALGORITMOS,
)
def test_algoritmo_preserva_todos_os_elementos(algoritmo):
    entrada = [8, 3, 8, 1, 0, 3, 5, 8, 2]
    resultado = algoritmo(entrada.copy())

    assert len(resultado) == len(entrada)
    assert sorted(resultado) == sorted(entrada)


def test_merge_sort_nao_modifica_a_lista_original():
    merge_sort = carregar_algoritmo(
        "merge_sort_immutability_module", "MergeSort.py", "merge_sort"
    )
    entrada = [4, 1, 3, 2]
    original = entrada.copy()

    resultado = merge_sort(entrada)

    assert resultado == [1, 2, 3, 4]
    assert entrada == original
    assert resultado is not entrada


def test_bucket_sort_nao_modifica_a_lista_original():
    bucket_sort = carregar_algoritmo(
        "bucket_sort_immutability_module", "BucketSort.py", "bucket_sort"
    )
    entrada = [4, 1, 3, 2]
    original = entrada.copy()

    resultado = bucket_sort(entrada)

    assert resultado == [1, 2, 3, 4]
    assert entrada == original
    assert resultado is not entrada
