using System;

namespace myproject
{
    class Program
    {
        static void Main(string[] args)
        {
            bool sair = false;
            while (!sair)
            {
                Console.WriteLine("Escolha uma operação: +, -, * ou /");
                string operacao = Console.ReadLine() ?? "";
                if (operacao.Equals("VITOR", StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Muito feio filho");
                    break;
                }

                Console.WriteLine("Operador A:");
                if (!double.TryParse(Console.ReadLine(), out double a))
                {
                    Console.WriteLine("Valor inválido.");
                    continue;
                }

                Console.WriteLine("Operador B:");
                if (!double.TryParse(Console.ReadLine(), out double b))
                {
                    Console.WriteLine("Valor inválido.");
                    continue;
                }

                try
                {
                    double resultado = Calculadora.Calcular(a, b, operacao);
                    Console.WriteLine("O resultado é: " + resultado.ToString("F2"));
                }
                catch (DivideByZeroException)
                {
                    Console.WriteLine("Erro: divisão por zero.");
                }
                catch (ArgumentException)
                {
                    Console.WriteLine("Operação inválida.");
                }

                Console.WriteLine("Deseja sair? S|N");
                sair = string.Equals(Console.ReadLine()?.Trim(), "S", StringComparison.OrdinalIgnoreCase);
            }
        }
    }
}
