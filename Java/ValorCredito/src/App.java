import java.util.Scanner;
import portfolio.logic.CalculadoraCredito;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Informe o seu saldo médio:");
        double saldo = input.nextDouble();
        input.close();
        try {
            System.out.printf("Seu valor de crédito é: %.2f%n", CalculadoraCredito.calcularCredito(saldo));
        } catch (IllegalArgumentException exception) {
            System.out.println("Valor inválido!");
        }
    }
}
