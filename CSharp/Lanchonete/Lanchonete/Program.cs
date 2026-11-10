using System;
using System.Collections.Generic;

namespace Lanchonete
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("------ Lanchonete ------");
            Console.WriteLine(" 1 | Sanduíche       R$ 5,00");
            Console.WriteLine(" 2 | Hambúrguer      R$ 10,00");
            Console.WriteLine(" 3 | Salada          R$ 7,00");
            Console.WriteLine(" 4 | Batata Frita    R$ 6,00");
            Console.WriteLine(" 5 | Almoço          R$ 15,00");
            Console.WriteLine(" 6 | Guarivata       R$ 3,00");
            Console.WriteLine(" 7 | Refrigerante    R$ 5,00");
            Console.WriteLine(" 8 | Suco            R$ 4,00");
            Console.WriteLine(" 9 | Água            R$ 2,00");
            Console.WriteLine("10 | Sorvete         R$ 6,00");
            Console.WriteLine("11 | Torta           R$ 8,00");
            Console.WriteLine("12 | Bolo            R$ 7,00");
            Console.WriteLine("13 | Pudim           R$ 9,00");

            Console.WriteLine("Informe seu nome:");
            string nome = Console.ReadLine() ?? "";
            List<int> pedidos = new List<int>();

            while (true)
            {
                Console.WriteLine("Informe o código do pedido ou S para finalizar:");
                string entrada = Console.ReadLine() ?? "";
                if (entrada.Trim().Equals("S", StringComparison.OrdinalIgnoreCase))
                    break;

                if (!int.TryParse(entrada, out int codigo) || !PedidoService.TryGetItem(codigo, out _))
                {
                    Console.WriteLine("Código inválido. Escolha um item de 1 a 13.");
                    continue;
                }
                pedidos.Add(codigo);
            }

            Console.WriteLine();
            Console.WriteLine(nome + ", seu pedido foi:");
            foreach (int codigo in pedidos)
            {
                PedidoService.TryGetItem(codigo, out ItemMenu item);
                Console.WriteLine(codigo + " | " + item.Nome + " - R$ " + item.Preco.ToString("F2"));
            }

            decimal total = PedidoService.CalcularTotal(pedidos);
            Console.WriteLine("Valor total: R$ " + total.ToString("F2"));
        }
    }
}
