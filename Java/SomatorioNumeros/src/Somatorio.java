import java.util.InputMismatchException;
import java.util.Scanner;

public class Somatorio {
    private int numero, soma;
    
    public Somatorio(int numero, int soma) {
        this.numero = numero;
        this.soma = soma;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getSoma() {
        return soma;
    }

    public void setSoma(int soma) {
        this.soma = soma;
    }
    
    public void entrada()  {
        
            Scanner entrada = new Scanner (System.in);

            while(this.numero > 0){

                System.out.println("\nNumero: ");

                try{
                    setNumero(entrada.nextInt());
                } 
                
                catch(InputMismatchException exception){
                    System.out.println("Entrada invalida!");
                    System.exit(0);
                }

                if (numero <= 0 ){
                  this.soma = soma - numero;
                }

                this.soma = soma + numero;
                System.out.println("\nSomatorio: "+ this.getSoma());
            }
    } 
}


