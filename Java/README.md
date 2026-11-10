# Java

Exercícios e projetos desenvolvidos em **Java**.

## Conteúdo
- `Alunos/`
- `Atleta/`
- `caneta/`
- `Carro/`
- `Computador/`
- `ContaCliente/`
- `ConversorTemperatura/`
- `Desktop/`
- `Ex46/`
- `Forno/`
- `GrupoTrabalho/`
- `IMC/`
- `Livros/`
- `Metodos/`
- `NumeroPrimo/`
- `SalarioMinimo/`
- `SomatorioNumeros/`
- `ValorCredito/`
- `common/` — regras reutilizáveis.
- `tests/` — testes automatizados com JUnit 5.

## Requisitos
- JDK 17 ou superior.
- Maven 3.9 ou superior para executar os testes.

## Testes automatizados
Os 32 testes JUnit cobrem conversão de temperatura, IMC, números primos, crédito bancário, conta de hotel e somatório.

A partir da raiz do repositório:

```bash
mvn -B -f Java/tests/pom.xml test
```

Os exercícios que utilizam regras compartilhadas importam as classes de `Java/common`. Para compilar e executar, por exemplo, o exercício de números primos no PowerShell, a partir da raiz do repositório:

```powershell
$fontes = Get-ChildItem "Java/common/src/main/java" -Recurse -Filter *.java | ForEach-Object FullName
New-Item -ItemType Directory -Force out | Out-Null
javac -encoding UTF-8 -d out $fontes "Java/NumeroPrimo/src/App.java"
java -cp out App
```

O GitHub Actions compila cada exercício Java separadamente e executa a suíte JUnit.
