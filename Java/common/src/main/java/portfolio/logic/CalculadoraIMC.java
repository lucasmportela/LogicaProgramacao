package portfolio.logic;

public final class CalculadoraIMC {
    private CalculadoraIMC() {}

    public static double calcular(double peso, double altura) {
        if (!Double.isFinite(peso) || !Double.isFinite(altura) || peso <= 0 || altura <= 0) {
            throw new IllegalArgumentException("Peso e altura devem ser valores positivos.");
        }
        return peso / (altura * altura);
    }

    public static String classificar(double imc) {
        if (!Double.isFinite(imc) || imc < 0) throw new IllegalArgumentException("IMC inválido.");
        if (imc < 18.5) return "Abaixo do peso!";
        if (imc < 25.0) return "Peso ideal!";
        if (imc < 30.0) return "Sobrepeso!";
        if (imc < 40.0) return "Obesidade!";
        return "Obesidade grave!";
    }
}
