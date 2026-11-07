import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Faça um programa em Java que leia o nome de uma pessoa, seu respectivo salário
        //bruto e o valor do salário mínimo, ao final calcular a quantidade de salários mínimos
        //recebida e exibir a mensagem:
        double quantidade, salario, minimo;
        String nome;

        Scanner input = new Scanner(System.in);
        System.out.println("Informe seu nome e salário bruto:");
        nome = input.nextLine();
        salario = input.nextDouble();
        System.out.println("Infome o valor do salário mínimo atual:");
        minimo = input.nextDouble();

        quantidade = salario / minimo;
        System.out.println(nome+" você recebe "+ String.format("%.2f", quantidade) +" salários mínimos");
        input.close();
    }
}
