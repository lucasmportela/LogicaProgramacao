import java.util.Scanner;
import portfolio.logic.ConversorTemperatura;

public class App {
    public static void main(String[] args) {
        System.out.println("Temperatura em Celsius a ser convertida em Fahrenheit:");
        Scanner input = new Scanner(System.in);
        double celsius = input.nextDouble();
        input.close();
        System.out.println("Temperatura em Fahrenheit: " + ConversorTemperatura.celsiusParaFahrenheit(celsius));
    }
}
