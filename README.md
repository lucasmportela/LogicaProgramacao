# Portfólio de Estudos e Projetos de Programação

[![CI](https://github.com/lucasmportela/LogicaProgramacao/actions/workflows/ci.yml/badge.svg)](https://github.com/lucasmportela/LogicaProgramacao/actions/workflows/ci.yml)

Repositório de exercícios, estudos e pequenos projetos desenvolvidos durante minha formação em programação.

O conteúdo está organizado por linguagem para facilitar a navegação.

## Linguagens e tecnologias

- [Python](Python/README.md)
- [Java](Java/README.md)
- [C](C/README.md)
- [C#](CSharp/README.md)
- [HTML e CSS](HTML/README.md)
- [JavaScript](JavaScript/README.md)
- [Portugol](Portugol/README.md)
- [C/C++ com OpenGL e GLUT](OpenGL-GLUT/README.md)

## Como utilizar

1. Acesse a pasta da linguagem desejada.
2. Escolha o exercício ou projeto.
3. Consulte o README interno, se existir.
4. Execute com a ferramenta adequada.

## Requisitos gerais

- Python 3 para os projetos Python.
- JDK para os projetos Java.
- GCC/MinGW ou outro compilador C/C++ para C e C++.
- .NET SDK para os projetos C#.
- Navegador moderno para HTML, CSS e JavaScript.
- Bibliotecas OpenGL/GLUT para os projetos gráficos.

## Testes automatizados em Python

Os algoritmos de ordenação possuem testes automatizados com **pytest**. A suíte cobre Bubble Sort, Quick Sort, Insertion Sort, Merge Sort, Heap Sort, Radix Sort, Bucket Sort, Shell Sort e Tim Sort.

Para executar os testes localmente, na raiz do repositório:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/python -v
```

Os testes verificam listas vazias, elementos únicos e repetidos, entradas ordenadas e invertidas, números negativos nos algoritmos compatíveis, valores decimais no Bucket Sort e validações do Radix Sort. O Bogo Sort não faz parte da execução automatizada porque seu tempo de execução é aleatório e não possui limite prático.

O GitHub Actions executa a suíte automaticamente em cada push e pull request para a branch `main`, além de verificar a sintaxe dos arquivos Python com `compileall`.

## Padrão de mensagens de commit

Este repositório utiliza **Conventional Commits** para manter o histórico claro e facilitar a identificação de funcionalidades, correções, testes e documentação.

Formato:

```text
tipo(escopo): descrição objetiva
```

Exemplos: `feat(python): adiciona busca binária`, `fix(python): corrige quick sort` e `test(python): amplia testes de ordenação`.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para conhecer os tipos recomendados e as orientações. O arquivo [`.gitmessage`](.gitmessage) oferece um modelo reutilizável para novos commits. Para ativá-lo neste repositório, execute `git config commit.template .gitmessage`.

## Organização do repositório

Foram removidos executáveis, arquivos de compilação, caches, pastas temporárias e arquivos ZIP internos. Os códigos-fonte e arquivos de dados foram mantidos.
