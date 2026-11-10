package portfolio.logic;

public final class CalculadoraCredito {
    private CalculadoraCredito() {}
    public static double calcularCredito(double saldoMedio) {
        if (!Double.isFinite(saldoMedio) || saldoMedio < 0) {
            throw new IllegalArgumentException("O saldo médio não pode ser negativo ou inválido.");
        }
        if (saldoMedio <= 2000.00) return 0.00;
        if (saldoMedio <= 4000.00) return saldoMedio * 0.20;
        if (saldoMedio <= 6000.00) return saldoMedio * 0.30;
        return saldoMedio * 0.40;
    }
}
