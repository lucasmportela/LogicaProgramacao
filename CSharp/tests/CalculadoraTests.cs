using System;
using myproject;
using Xunit;

namespace CSharp.Tests;

public class CalculadoraTests
{
    [Theory]
    [InlineData(2, 3, "+", 5)]
    [InlineData(8, 3, "-", 5)]
    [InlineData(4, 3, "*", 12)]
    [InlineData(12, 3, "/", 4)]
    [InlineData(-5, 2, "+", -3)]
    public void Calcular_DeveExecutarOperacoesValidas(double a, double b, string operacao, double esperado)
    {
        Assert.Equal(esperado, Calculadora.Calcular(a, b, operacao), 8);
    }

    [Fact]
    public void Calcular_DivisaoPorZero_DeveLancarExcecao()
    {
        Assert.Throws<DivideByZeroException>(() => Calculadora.Calcular(10, 0, "/"));
    }

    [Fact]
    public void Calcular_OperacaoDesconhecida_DeveLancarExcecao()
    {
        Assert.Throws<ArgumentException>(() => Calculadora.Calcular(2, 2, "%"));
    }
}
