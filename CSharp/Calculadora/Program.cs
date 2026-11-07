using System;

namespace myproject
{
    class Program
    {
        static void Main(string[] args)
        {
            double result = 0, a, b = 0;
            string oper, sair = "a";

            while (sair != "S")
            {
                Console.WriteLine("Escolha uma operação:");
                Console.WriteLine("+ = soma");
                Console.WriteLine("- = subtração");
                Console.WriteLine("* = multiplicação");
                Console.WriteLine("/ = divisão");
                oper = Console.ReadLine();
                if (oper == "VITOR")
                    {
                        Console.WriteLine("Muito feio filho");
                        Console.ReadKey();
                        sair = "S";
                    }

                while (sair != "S")
                {
                    Console.Clear();
                    Console.WriteLine("Operador A:");
                    a = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine("Operador B:");
                    b = Convert.ToDouble(Console.ReadLine());
                    if (oper == "+")
                    {
                        result = a + b;
                    }
                    else if (oper == "-")
                    {
                        result = a - b;
                    }
                    else if (oper == "*")
                    {
                        result = a * b;
                    }
                    else if (oper == "/")
                    {
                        result = a / b;
                    }
                    Console.WriteLine("O resultado é: " + result.ToString("F2"));
                    Console.WriteLine("Deseja sair? S|N");
                    sair = Console.ReadLine();
                }
                Console.Clear();
                sair = "a";
                Console.WriteLine("Deseja sair? S|N");
                sair = Console.ReadLine();
                Console.Clear();
            }
        }
    }
}
