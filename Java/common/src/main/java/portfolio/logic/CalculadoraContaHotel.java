package portfolio.logic;

public final class CalculadoraContaHotel {
    private static final double VALOR_DIARIA = 160.00;
    private CalculadoraContaHotel() {}

    public static double calcularTotal(int quantidadeDiarias) {
        if (quantidadeDiarias <= 0) {
            throw new IllegalArgumentException("A quantidade de diárias deve ser positiva.");
        }
        double taxaServico = quantidadeDiarias > 15 ? 55.00
            : quantidadeDiarias == 15 ? 60.00 : 80.00;
        return (VALOR_DIARIA + taxaServico) * quantidadeDiarias;
    }
}
