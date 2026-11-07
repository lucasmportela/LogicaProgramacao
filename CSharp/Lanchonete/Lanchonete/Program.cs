using System;

namespace Lanchonete
{
    class Program
    {
        static void Main(string[] args)
        {
            string nome, sair = "a";
            string[] pedido = new string[10];
            int x = 0;
            double valor = 0.00;


            Console.WriteLine("------Lanchonete------");
            Console.WriteLine("\n--------Comida--------");
            Console.WriteLine("1|Sanduiche      R$5,00");
            Console.WriteLine("2|Hamburguer     R$10,00");
            Console.WriteLine("3|Salada         R$7,00");
            Console.WriteLine("4|Batata Frita   R$6,00");
            Console.WriteLine("5|Almoço         R$15,00");
            Console.WriteLine("--------Bebida--------");
            Console.WriteLine("6|Guarivata      R$3,00");
            Console.WriteLine("7|Refrigerante   R$5,00");
            Console.WriteLine("8|Suco           R$4,00");
            Console.WriteLine("9|Água           R$2,00");
            Console.WriteLine("-------Sobremesa------");
            Console.WriteLine("10|Sorvete       R$6,00");
            Console.WriteLine("11|Torta         R$8,00");
            Console.WriteLine("12|Bolo          R$7,00");
            Console.WriteLine("13|Pudim         R$9,00");

            Console.WriteLine("Informe seu nome:");
            nome = Console.ReadLine();

            while (sair != "S")
            {
                Console.WriteLine("Informe seu pedido:");
                pedido[x] = Convert.ToString(Console.ReadLine());
                x = x + 1;
                sair = Console.ReadLine();
            }
            Console.Clear();
            Console.WriteLine(nome + " seu pedido foi:");
            x = 0;
            while (x < 10)
                {
                if (pedido[x] == "1")
                {
                    valor = valor + 5.00;
                    Console.WriteLine("1|Sanduiche      R$5,00");
                }
                else if (pedido[x] == "2")
                {
                    valor = valor + 10.00;
                    Console.WriteLine("2|Hamburguer     R$10,00");
                }
                else if (pedido[x] == "3")
                {
                    valor = valor + 7.00;
                    Console.WriteLine("3|Salada         R$7,00");
                }
                else if (pedido[x] == "4")
                {
                    valor = valor + 6.00;
                    Console.WriteLine("4|Batata Frita   R$6,00");
                }
                else if (pedido[x] == "5")
                {
                    valor = valor + 15.00;
                    Console.WriteLine("5|Almoço         R$15,00");
                }
                else if (pedido[x] == "6")
                {
                    valor = valor + 3.00;
                    Console.WriteLine("6|Guarivata      R$3,00");
                }
                else if (pedido[x] == "7")
                {
                    valor = valor + 5.00;
                    Console.WriteLine("7|Refrigerante   R$5,00");
                }
                else if (pedido[x] == "8")
                {
                    valor = valor + 4.00;
                    Console.WriteLine("8|Suco           R$4,00");
                }
                else if (pedido[x] == "9")
                {
                    valor = valor + 2.00;
                    Console.WriteLine("9|Água           R$2,00");
                }
                else if (pedido[x] == "10")
                {
                    valor = valor + 6.00;
                    Console.WriteLine("10|Sorvete       R$6,00");
                }
                else if (pedido[x] == "11")
                {
                    valor = valor + 8.00;
                    Console.WriteLine("11|Torta         R$8,00");
                }
                else if (pedido[x] == "12")
                {
                    valor = valor + 7.00;
                    Console.WriteLine("12|Bolo          R$7,00");
                }
                else if (pedido[x] == "13")
                {
                    valor = valor + 9.00;
                    Console.WriteLine("13|Pudim         R$9,00");
                }
                x = x + 1;
            }
            Console.WriteLine("Valor total: " + valor.ToString("F2"));
            Console.ReadKey();
        }
    }
}
