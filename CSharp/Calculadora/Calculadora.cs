namespace myproject
{
    public static class Calculadora
    {
        public static double Calcular(double a, double b, string operacao)
        {
            return operacao switch
            {
                "+" => a + b,
                "-" => a - b,
                "*" => a * b,
                "/" when b != 0 => a / b,
                "/" => throw new DivideByZeroException("Não é possível dividir por zero."),
                _ => throw new ArgumentException("Operação inválida.", nameof(operacao))
            };
        }
    }
}
