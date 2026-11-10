package portfolio.logic;

public final class ConversorTemperatura {
    private ConversorTemperatura() {}
    public static double celsiusParaFahrenheit(double celsius) {
        return (9 * celsius + 160) / 5;
    }
}
