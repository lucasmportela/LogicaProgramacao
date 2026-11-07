import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Um hotel cobra R$ 160.00 a diária e mais uma taxa de serviços. A taxa de serviços é de:
        //•R$ 55,00 por diária, se o número de diárias for maior que 15;
        //• R$ 60,00 por diária, se o número de diárias for igual a 15;
        //•R$ 80,00 por diária, se o número de diárias for menor que 15.
        //Construa um programa em Java que mostre o nome e o total da conta de um cliente.

        String nome;
        int diarias;
        double valor;

        Scanner input = new Scanner(System.in);
        System.out.println("Informe seu nome e a quantidade de diárias:");
        nome = input.nextLine();
        diarias = input.nextInt();

        if (diarias > 15){

            valor = (150.00*diarias) + (55.50*diarias);
        }
        else if (diarias < 15){

            valor = (150.00*diarias) + (80.00*diarias);
        }else{
            
            valor = (150.00*diarias) + (60.00*diarias);
        }
        System.out.println(nome + " sua conta é no valor de: " + valor);
        input.close();
    }
}
