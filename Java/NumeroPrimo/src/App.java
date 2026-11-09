import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        int numero;

        Scanner input = new Scanner(System.in);
        System.out.println("Digite um número:");
        numero = input.nextInt();

        if (numero == 2 || numero == 3){

            System.out.println(numero + " é primo!");
        
        }else if (numero % 2 == 0 || numero % 3 == 0){

            System.out.println(numero + " não é primo!");

        } else if(numero % 2 != 0 || numero % 3 != 0){

            System.out.println(numero + " é primo!");

        } else{

            System.out.println("Número invalido!");

        }

        input.close();
    }
}
