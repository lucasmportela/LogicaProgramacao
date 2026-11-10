package portfolio.logic;

public final class VerificadorPrimo {
    private VerificadorPrimo() {}
    public static boolean isPrimo(int numero) {
        if (numero < 2) return false;
        if (numero == 2) return true;
        if (numero % 2 == 0) return false;
        for (int divisor = 3; divisor <= numero / divisor; divisor += 2) {
            if (numero % divisor == 0) return false;
        }
        return true;
    }
}
