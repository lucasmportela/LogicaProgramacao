# C#

Exercícios e projetos desenvolvidos em **C#**.

## Conteúdo

- `Calculadora/`
- `Lanchonete/`
- `Média/`

## Requisitos

- .NET 10 SDK ou superior.

## Compilação e execução

A partir da raiz do repositório, compile cada projeto com:

```bash
dotnet build "CSharp/Calculadora/teste.csproj" --configuration Release
dotnet build "CSharp/Lanchonete/Lanchonete/Lanchonete.csproj" --configuration Release
dotnet build "CSharp/Média/teste.csproj" --configuration Release
```

Para executar um projeto, utilize `dotnet run --project` seguido do caminho do arquivo `.csproj`. Exemplo:

```bash
dotnet run --project "CSharp/Calculadora/teste.csproj"
```

Todos os projetos C# deste repositório utilizam o target framework `net10.0`.

Arquivos executáveis, saídas de compilação e caches foram removidos; os códigos-fonte e arquivos de dados foram preservados.
