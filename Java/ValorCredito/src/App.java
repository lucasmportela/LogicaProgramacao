import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        //Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio
        //no último ano. Faça um programa em Java que leia o saldo médio de um cliente e calcule
        //o valor do crédito de acordo com a tabela abaixo. Mostre uma mensagem informando o
        //saldo médio e o valor do crédito.
        //Saldo médio Percentual
        //de 4000.01 a 6000.01 30% do valor do saldo médio
        //acima de 6000.00 40% do valor do saldo médio
        //de 0 a 2000.00 nenhum crédito
        //de 2000.01 a 4000.00 20% do valor do saldo médio

        double saldo, credito = 0;

        Scanner input = new Scanner(System.in);
        System.out.println("Informe o seu saldo médio:");
        saldo = input.nextDouble();

        if (saldo > 6000.00){

            credito = saldo * 0.40;
            
        } else if (saldo > 4000.01 && saldo < 6000.01){
            
            credito = saldo * 0.30;

        } else if(saldo > 2000.01 && saldo < 5000.00){

            credito = saldo * 0.20;

        } else if(saldo > 0 && saldo <= 2000.00){

            credito = 0.00;

        } else{
            System.out.println("Valor Invalido!");
        }

        System.out.println("Seu valor de crédito é: "+ String.format("%.2f", credito));


        input.close();

    }

}
