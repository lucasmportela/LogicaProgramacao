using System;

Console.WriteLine("Informe seu nome:");
string nome = Console.ReadLine() ?? "";

double prova1;
double prova2;
while (true)
{
    Console.WriteLine("Primeira prova:");
    if (!double.TryParse(Console.ReadLine(), out prova1))
    {
        Console.WriteLine("Valor inválido.");
        continue;
    }
    Console.WriteLine("Segunda prova:");
    if (!double.TryParse(Console.ReadLine(), out prova2))
    {
        Console.WriteLine("Valor inválido.");
        continue;
    }
    if (CalculadoraMedia.NotasProvasValidas(prova1, prova2)) break;
    Console.WriteLine("As notas das provas devem estar entre 0 e 10.");
}

double simulado;
double pontosExtra;
while (true)
{
    Console.WriteLine("Simulado:");
    if (!double.TryParse(Console.ReadLine(), out simulado))
    {
        Console.WriteLine("Valor inválido.");
        continue;
    }
    Console.WriteLine("Pontos extra:");
    if (!double.TryParse(Console.ReadLine(), out pontosExtra))
    {
        Console.WriteLine("Valor inválido.");
        continue;
    }
    if (CalculadoraMedia.SimuladoEExtraValidos(simulado, pontosExtra)) break;
    Console.WriteLine("O simulado deve estar entre 0 e 7 e os pontos extras entre 0 e 3.");
}

double media = CalculadoraMedia.Calcular(prova1, prova2, simulado, pontosExtra);
string resultado = CalculadoraMedia.Classificar(media);
if (resultado == "Aprovado")
    Console.WriteLine("Parabéns " + nome + " você foi aprovado");
else if (resultado == "Recuperação")
    Console.WriteLine(nome + " você está de recuperação");
else
    Console.WriteLine(nome + " você foi reprovado");
Console.WriteLine("Sua média é: " + media.ToString("F2"));
