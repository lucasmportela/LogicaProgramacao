using System;

public static class CalculadoraMedia
{
    public static bool NotasProvasValidas(double prova1, double prova2)
    {
        return double.IsFinite(prova1) && double.IsFinite(prova2)
            && prova1 >= 0 && prova1 <= 10 && prova2 >= 0 && prova2 <= 10;
    }

    public static bool SimuladoEExtraValidos(double simulado, double pontosExtra)
    {
        return double.IsFinite(simulado) && double.IsFinite(pontosExtra)
            && simulado >= 0 && simulado <= 7 && pontosExtra >= 0 && pontosExtra <= 3;
    }

    public static double Calcular(double prova1, double prova2, double simulado, double pontosExtra)
    {
        if (!NotasProvasValidas(prova1, prova2))
            throw new ArgumentOutOfRangeException(nameof(prova1));
        if (!SimuladoEExtraValidos(simulado, pontosExtra))
            throw new ArgumentOutOfRangeException(nameof(simulado));

        double mediaProvas = (prova1 + prova2) / 2;
        return (mediaProvas + simulado + pontosExtra) / 2;
    }

    public static string Classificar(double media)
    {
        if (!double.IsFinite(media) || media < 0)
            throw new ArgumentOutOfRangeException(nameof(media));
        if (media >= 7) return "Aprovado";
        if (media >= 5) return "Recuperação";
        return "Reprovado";
    }
}
