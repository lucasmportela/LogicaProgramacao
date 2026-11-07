import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Faça um programa em Java que leia uma temperatura em graus Célsius e apresentá-la
        //convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5. Onde F é a
        //temperatura em Fahrenheit e C é a temperatura em Célsius.
        float temp;


        System.out.println("Temperatura em Célsius a ser convertida em Fahrenheit:");
        Scanner input = new Scanner(System.in);
        temp = input.nextFloat();
        input.close();

        temp = (9*temp+160)/5;

        System.out.println("Temperatura em Fahrenheit: "+ temp);


    }
}
