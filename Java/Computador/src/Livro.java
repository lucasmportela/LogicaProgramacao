import java.util.Scanner;

public class Livro {

    private int codigo;
    private String descricao;
    private double peso;
    private double preco;
    private String autor;

    
    public Livro(int codigo, String descricao, double peso, double preco, String autor) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.peso = peso;
        this.preco = preco;
        this.autor = autor;
    }

    public int getCodigo() {
        return codigo;
    }
    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }


    public void entrada(){

        Scanner entrada = new Scanner(System.in);

        System.out.println("\n-----Dados do Livro------");
        System.out.println("Codigo: "+ );
    }
}
