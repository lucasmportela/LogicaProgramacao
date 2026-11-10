import java.util.Scanner;
import portfolio.logic.VerificadorPrimo;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite um número:");
        int numero = input.nextInt();
        System.out.println(numero + (VerificadorPrimo.isPrimo(numero) ? " é primo!" : " não é primo!"));
        input.close();
    }
}
