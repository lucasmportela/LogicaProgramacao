import java.util.InputMismatchException;
import java.util.Scanner;
import portfolio.logic.CalculadoraSomatorio;

public class Somatorio {
    private int numero;
    private int soma;

    public Somatorio(int numero, int soma) {
        this.numero = numero;
        this.soma = soma;
    }
    public int getNumero() { return numero; }
    public void setNumero(int numero) { this.numero = numero; }
    public int getSoma() { return soma; }
    public void setSoma(int soma) { this.soma = soma; }

    public void entrada() {
        Scanner entrada = new Scanner(System.in);
        while (numero > 0) {
            System.out.println("\nNúmero: ");
            try {
                setNumero(entrada.nextInt());
            } catch (InputMismatchException exception) {
                System.out.println("Entrada inválida!");
                return;
            }
            if (numero <= 0) break;
            soma = CalculadoraSomatorio.adicionar(soma, numero);
            System.out.println("\nSomatório: " + getSoma());
        }
    }
}
