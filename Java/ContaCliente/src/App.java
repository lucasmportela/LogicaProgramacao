import java.util.Scanner;
import portfolio.logic.CalculadoraContaHotel;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Informe seu nome:");
        String nome = input.nextLine();
        System.out.println("Informe a quantidade de diárias:");
        int diarias = input.nextInt();
        input.close();
        try {
            double total = CalculadoraContaHotel.calcularTotal(diarias);
            System.out.printf("%s sua conta é no valor de: R$ %.2f%n", nome, total);
        } catch (IllegalArgumentException exception) {
            System.out.println(exception.getMessage());
        }
    }
}
