import java.util.Scanner;
import portfolio.logic.CalculadoraIMC;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (true) {
            System.out.println("IMC = Peso / (Altura x Altura)");
            System.out.println("Digite sua altura:");
            double altura = input.nextDouble();
            System.out.println("Digite seu peso:");
            double peso = input.nextDouble();
            try {
                double imc = CalculadoraIMC.calcular(peso, altura);
                System.out.printf("IMC: %.2f%n", imc);
                System.out.println(CalculadoraIMC.classificar(imc));
            } catch (IllegalArgumentException exception) {
                System.out.println(exception.getMessage());
            }
            System.out.println("Deseja sair? Digite 1 para sair.");
            if (input.nextInt() == 1) break;
        }
        input.close();
    }
}
