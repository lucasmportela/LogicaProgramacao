import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String Nome;
        Double Altura, Peso;

        System.out.println("Digite seu nome:");
        Nome = input.nextLine();

        System.out.println("Digite sua altura:");
        Altura = input.nextDouble();
        
        System.out.println("Digite seu peso:");
        Peso = input.nextDouble();

        System.out.println(Peso);
        System.out.println(Altura);
        System.out.println(Nome);

        input.close();

    }
    
}
