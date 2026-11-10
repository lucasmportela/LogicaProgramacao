using System;
using Xunit;

namespace CSharp.Tests;

public class CalculadoraMediaTests
{
    [Theory]
    [InlineData(0, 10, true)]
    [InlineData(7.5, 8, true)]
    [InlineData(-1, 8, false)]
    [InlineData(8, 10.1, false)]
    public void NotasProvasValidas_DeveValidarLimites(double prova1, double prova2, bool esperado)
    {
        Assert.Equal(esperado, CalculadoraMedia.NotasProvasValidas(prova1, prova2));
    }

    [Theory]
    [InlineData(0, 0, true)]
    [InlineData(7, 3, true)]
    [InlineData(7.1, 2, false)]
    [InlineData(5, -1, false)]
    public void SimuladoEExtraValidos_DeveValidarLimites(double simulado, double extra, bool esperado)
    {
        Assert.Equal(esperado, CalculadoraMedia.SimuladoEExtraValidos(simulado, extra));
    }

    [Fact]
    public void Calcular_DeveAplicarFormulaDasNotas()
    {
        Assert.Equal(7.0, CalculadoraMedia.Calcular(8, 6, 5, 2), 8);
    }

    [Fact]
    public void Calcular_NotasInvalidas_DeveLancarExcecao()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => CalculadoraMedia.Calcular(11, 6, 5, 2));
    }

    [Theory]
    [InlineData(7, "Aprovado")]
    [InlineData(5, "Recuperação")]
    [InlineData(4.99, "Reprovado")]
    public void Classificar_DeveRetornarSituacaoCorreta(double media, string esperado)
    {
        Assert.Equal(esperado, CalculadoraMedia.Classificar(media));
    }
}
