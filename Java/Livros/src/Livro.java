import java.util.Scanner;

public class Livro {
      
    private String autor;
    private double preco;
    private String editora;

    public Livro(String autor, double preco, String editora) {

        this.autor = autor;
        this.preco = preco;
        this.editora = editora;

    }

    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }
    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public String getEditora() {
        return editora;
    }
    public void setEditora(String editora) {
        this.editora = editora;
    }

     public void entrada() {

        Scanner entrada = new Scanner( System.in );

        System.out.println("\n-----Entrada de Dados:-----");
        System.out.println("Autor: ");
        setAutor(entrada.next());

        System.out.println("Editora: ");
        setEditora(entrada.next());

        System.out.println("Preço: ");
        setPreco(entrada.nextDouble());

     }

     public void imprimir(){
        System.out.println("\n------Dados do livro:------");
        System.out.println("Autor: "+ this.getAutor());
        System.out.println("Editora: "+ this.getEditora());
        System.out.println("Preço: "+ this.getPreco());
    }
}
