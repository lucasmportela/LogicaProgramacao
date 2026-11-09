import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        try (Scanner entrada = new Scanner(System.in)) {

            CD c1 = new CD(0, null, 0, 0, null);

            c1.entrada(entrada);
            c1.saida();

        }
    }
}