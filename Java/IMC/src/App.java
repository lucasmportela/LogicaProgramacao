import java.util.Scanner;

public class App {
    public static void main(String[] args) {

            Scanner input = new Scanner(System.in);
            Double IMC, Peso, Altura;
            Integer Sair = 0;

            while(Sair  != 1){
                System.out.println("IMC = Peso /(Altura x Altura)");

                System.out.println("Digite sua altura:");
                Altura = input.nextDouble();

                System.out.println("Digite seu peso:");
                Peso = input.nextDouble();

                IMC = Peso / (Altura * Altura);
                System.out.println("IMC:");
                System.out.format("%.2f\n",IMC);

                if (IMC < 18.50){
                    System.out.println("Abaixo do peso!");
                }
                else if(IMC < 24.90){
                    System.out.println("Peso ideal!");
                }
                else if(IMC < 29.90){
                    System.out.println("Sobrepeso!");
                }
                else if(IMC < 39.90){
                    System.out.println("Obesidade!");
                }
                else if(IMC > 40.00){
                    System.out.println("Obesidade grave!");
                }
                else{
                    System.out.println("Erro!");
                }
                System.out.println("Deseja sair? 1");
                Sair = input.nextInt();
            }
            input.close();
        }    
}
