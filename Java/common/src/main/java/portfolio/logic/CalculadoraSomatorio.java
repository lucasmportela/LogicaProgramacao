package portfolio.logic;

public final class CalculadoraSomatorio {
    private CalculadoraSomatorio() {}
    public static int adicionar(int totalAtual, int valor) {
        if (totalAtual < 0 || valor <= 0) {
            throw new IllegalArgumentException("O total não pode ser negativo e o valor deve ser positivo.");
        }
        return Math.addExact(totalAtual, valor);
    }
}
