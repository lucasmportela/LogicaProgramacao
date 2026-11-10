using System.Collections.Generic;

namespace Lanchonete
{
    public sealed class ItemMenu
    {
        public ItemMenu(string nome, decimal preco)
        {
            Nome = nome;
            Preco = preco;
        }

        public string Nome { get; }
        public decimal Preco { get; }
    }

    public static class PedidoService
    {
        private static readonly IReadOnlyDictionary<int, ItemMenu> Itens =
            new Dictionary<int, ItemMenu>
            {
                [1] = new ItemMenu("Sanduíche", 5.00m),
                [2] = new ItemMenu("Hambúrguer", 10.00m),
                [3] = new ItemMenu("Salada", 7.00m),
                [4] = new ItemMenu("Batata Frita", 6.00m),
                [5] = new ItemMenu("Almoço", 15.00m),
                [6] = new ItemMenu("Guarivata", 3.00m),
                [7] = new ItemMenu("Refrigerante", 5.00m),
                [8] = new ItemMenu("Suco", 4.00m),
                [9] = new ItemMenu("Água", 2.00m),
                [10] = new ItemMenu("Sorvete", 6.00m),
                [11] = new ItemMenu("Torta", 8.00m),
                [12] = new ItemMenu("Bolo", 7.00m),
                [13] = new ItemMenu("Pudim", 9.00m)
            };

        public static bool TryGetItem(int codigo, out ItemMenu item)
        {
            if (Itens.TryGetValue(codigo, out ItemMenu encontrado))
            {
                item = encontrado;
                return true;
            }
            item = new ItemMenu("Item inválido", 0m);
            return false;
        }

        public static decimal CalcularTotal(IEnumerable<int> codigos)
        {
            decimal total = 0m;
            foreach (int codigo in codigos)
            {
                if (TryGetItem(codigo, out ItemMenu item))
                    total += item.Preco;
            }
            return total;
        }
    }
}
