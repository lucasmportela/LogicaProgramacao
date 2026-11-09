# Python

Exercícios e projetos desenvolvidos em **Python**.

## Conteúdo

- `AcimaDaMedia/`
- `AdivinharNúmero/`
- `AlgorítmosDeOrdenação/`
- `Almoxarifado/`
- `AnaliseDeDesempenhoDeEscola/`
- `AnaliseTemperaturaSemana/`
- `Arquivos/`
- `Arvore/`
- `AteCem/`
- `AV1/`
- `BairroOrdemAlfabetica/`
- `BancoPython/`
- `BoletimCSV/`
- `BuscaElemento/`
- `CadastroFuncionarioEscola/`
- `CalculadoraFunção/`
- `CalculadoraPython/`
- `ConfiBancoTupla/`
- `ContaBancaria/`
- `ContagemRegressiva/`
- `ControleDePermissõesDeAcesso/`
- `DescontoProduto/`
- `DetectaçãoDeEntrada/`
- `DezAteZero/`
- `Dicionario/`
- `Fatorial/`
- `FiboDeZeroAteDoisMil/`
- `Fibonacci/`
- `FilaDeTarefaDeSistemas/`
- `FormularioWebDespadronizado/`
- `FrequênciaElementoEmLista/`
- `IdadeAte2040/`
- `IMC/`
- `InversaoDeVetor/`
- `InversãoMatriz/`
- `Jogo/`
- `ListaEmails/`
- `Loja/`
- `LojaDeRoupas/`
- `MaiorDeIdade/`
- `MaiorDeIdadeClasse/`
- `MaiorEMenor/`
- `MaiorOuMenorIndice/`
- `MaiorQueDez/`
- `MaiorTresNumeros/`
- `MaisNovo/`
- `Maquinario/`
- `Matrizes/`
- `MediaCincoAlunos/`
- `MediaDezNumeros/`
- `MediaEContagem/`
- `MediaNota/`
- `MediaNotaDezAlunos/`
- `ModuloDeTriagemDeRecrutamento/`
- `MonitoramentoEficiênciaDeFrotas/`
- `MonitoramentoTermicoDeServidores/`
- `NomeCidade/`
- `NotaAlunoPrivate/`
- `NotaZeroAteDez/`
- `NumeroAoCubo/`
- `NumeroAoQuadrado/`
- `NumeroÍmparesVetor/`
- `OrdemCrescente/`
- `PadrãoTexto/`
- `ParAteZero/`
- `ParOuImpar/`
- `ParOuImparSeteNumeros/`
- `PedraPapelTesoura/`
- `PlantaIndustrialCaixa/`
- `PortasLogicas/`
- `ProcessamentoDePonteDeVenda/`
- `ProgramasGráficos/`
- `RegistrarAcessoTXT/`
- `RendaMensal/`
- `ReposiçãoAlmoxarifado/`
- `SalarioAumentoDe15%/`
- `SalarioDesconto/`
- `Saudacoes/`
- `SistemaCorporativo/`
- `SistemaDeAutenticação/`
- `SistemaDeMonitoramentoDeBateria/`
- `SistemaFaturamentoComercial/`
- `somaDoisNumerosFunção/`
- `SomatorioCondicional/`
- `SubprogramasAninhados/`
- `SubstituicaoValoresNegativos/`
- `Tabuada/`
- `TresValoresNumericos/`
- `TrêsAlunosTXT/`
- `VendasBruto/`

## Execução

Consulte o README de cada projeto, quando disponível. Para os exercícios sem documentação própria, utilize o compilador, interpretador ou ferramenta correspondente à linguagem.

## Testes automatizados

Os testes automatizados dos algoritmos de ordenação ficam em [`tests/python/`](../tests/python/). A suíte utiliza **pytest** e atualmente contém **102 casos de teste**.

Na raiz do repositório, instale as dependências de desenvolvimento e execute:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/python -v
```

Para verificar a sintaxe de todos os arquivos Python:

```bash
python -m compileall -q .
```

Consulte o [guia dos testes Python](../tests/python/README.md) para ver os algoritmos cobertos, os cenários validados e como manter a documentação atualizada quando a suíte mudar.

Arquivos executáveis, saídas de compilação e caches foram removidos; os códigos-fonte e arquivos de dados foram preservados.
