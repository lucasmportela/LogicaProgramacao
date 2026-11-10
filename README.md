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
- .NET 10 SDK ou superior para os projetos C#.
- Navegador moderno para HTML, CSS e JavaScript.
- Bibliotecas OpenGL/GLUT para os projetos gráficos.

## Projetos C#

Os três projetos C# utilizam **.NET 10 (LTS)**. Para compilar todos, execute a partir da raiz:

```bash
dotnet build "CSharp/Calculadora/teste.csproj" --configuration Release
dotnet build "CSharp/Lanchonete/Lanchonete/Lanchonete.csproj" --configuration Release
dotnet build "CSharp/Média/teste.csproj" --configuration Release
```

Consulte [CSharp/README.md](CSharp/README.md) para os comandos de execução.

## Testes automatizados em C# e Java

Os projetos C# possuem **50 casos de teste com xUnit** para a calculadora, a lanchonete e a média escolar:

```bash
dotnet test "CSharp/tests/CSharp.Tests.csproj" --configuration Release
```

Os exercícios Java compartilham regras testáveis em `Java/common` e possuem **33 testes com JUnit 5** para conversão de temperatura, IMC, números primos, crédito bancário, conta de hotel e somatório:

```bash
mvn -B -f Java/tests/pom.xml test
```

O GitHub Actions compila os projetos C# e Java e executa as duas suítes a cada push e pull request direcionado à branch `main`.

## Testes automatizados em Python

Os algoritmos de ordenação possuem uma suíte automatizada com **pytest**. Atualmente, ela contém **102 casos de teste** para nove algoritmos: Bubble Sort, Quick Sort, Insertion Sort, Merge Sort, Heap Sort, Radix Sort, Bucket Sort, Shell Sort e Tim Sort.

Para executar as verificações a partir da raiz do repositório:

```bash
python -m pip install -r requirements-dev.txt
python -m compileall -q .
python -m pytest tests/python -v
```

A suíte verifica listas vazias, elementos únicos e repetidos, listas ordenadas e invertidas, números negativos nos algoritmos compatíveis, valores decimais no Bucket Sort, validações de entrada do Radix Sort e preservação dos elementos. Também verifica que Merge Sort e Bucket Sort não alteram a lista original.

O Radix Sort aceita somente números inteiros não negativos. O Bucket Sort também é testado com valores negativos e decimais. O total de testes informado acima representa o estado atual da suíte e deve ser atualizado quando novos casos forem adicionados ou removidos.

O GitHub Actions executa a verificação de sintaxe com `compileall` e os testes com `pytest` em cada push e pull request direcionado à branch `main`. A suíte, seus cenários e as orientações para atualizar esta documentação estão descritos em [tests/python/README.md](tests/python/README.md).

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
