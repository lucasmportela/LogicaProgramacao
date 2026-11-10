using System.Collections.Generic;
using Lanchonete;
using Xunit;

namespace CSharp.Tests;

public class PedidoServiceTests
{
    [Theory]
    [InlineData(1, "Sanduíche", 5.00)]
    [InlineData(2, "Hambúrguer", 10.00)]
    [InlineData(3, "Salada", 7.00)]
    [InlineData(4, "Batata Frita", 6.00)]
    [InlineData(5, "Almoço", 15.00)]
    [InlineData(6, "Guarivata", 3.00)]
    [InlineData(7, "Refrigerante", 5.00)]
    [InlineData(8, "Suco", 4.00)]
    [InlineData(9, "Água", 2.00)]
    [InlineData(10, "Sorvete", 6.00)]
    [InlineData(11, "Torta", 8.00)]
    [InlineData(12, "Bolo", 7.00)]
    [InlineData(13, "Pudim", 9.00)]
    public void TryGetItem_CodigoValido_DeveRetornarItem(int codigo, string nome, double preco)
    {
        Assert.True(PedidoService.TryGetItem(codigo, out ItemMenu item));
        Assert.Equal(nome, item.Nome);
        Assert.Equal((decimal)preco, item.Preco);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    [InlineData(99)]
    public void TryGetItem_CodigoInvalido_DeveRetornarFalso(int codigo)
    {
        Assert.False(PedidoService.TryGetItem(codigo, out _));
    }

    [Fact]
    public void CalcularTotal_DeveSomarTodosOsItens()
    {
        Assert.Equal(24.00m, PedidoService.CalcularTotal(new[] { 1, 2, 13 }));
    }

    [Fact]
    public void CalcularTotal_ListaVazia_DeveRetornarZero()
    {
        Assert.Equal(0m, PedidoService.CalcularTotal(new List<int>()));
    }

    [Fact]
    public void CalcularTotal_DeveIgnorarCodigosInvalidos()
    {
        Assert.Equal(15.00m, PedidoService.CalcularTotal(new[] { 1, 99, 2, -1 }));
    }

    [Fact]
    public void CalcularTotal_DeveSomarItensRepetidos()
    {
        Assert.Equal(15.00m, PedidoService.CalcularTotal(new[] { 1, 1, 1 }));
    }
}
