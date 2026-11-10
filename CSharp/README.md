# C#

Exercícios e projetos desenvolvidos em **C#**.

## Conteúdo
- `Calculadora/`
- `Lanchonete/`
- `Média/`
- `tests/` — testes automatizados com xUnit.

## Requisitos
- .NET 10 SDK ou superior.

## Compilação e execução
A partir da raiz do repositório:

```bash
dotnet build "CSharp/Calculadora/teste.csproj" --configuration Release
dotnet build "CSharp/Lanchonete/Lanchonete/Lanchonete.csproj" --configuration Release
dotnet build "CSharp/Média/teste.csproj" --configuration Release
dotnet run --project "CSharp/Calculadora/teste.csproj"
```

## Testes automatizados
A suíte xUnit cobre as operações da calculadora, preços e totais da lanchonete, validações e classificação da média escolar.

```bash
dotnet test "CSharp/tests/CSharp.Tests.csproj" --configuration Release
```
