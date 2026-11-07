import java.util.Scanner;

public class CD {
    private int codigo;
    private String descricao;
    private double peso;
    private double preco;
    private String banda;

    public CD(int codigo, String descricao, double peso, double preco, String banda) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.peso = peso;
        this.preco = preco;
        this.banda = banda;
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
    public String getBanda() {
        return banda;
    }
    public void setBanda(String banda) {
        this.banda = banda;
    }

    public void entrada (){

        Scanner entrada = new Scanner (System.in);

        System.out.println("\n-------Dados do CD--------");

        System.out.println("Código: ");
        setCodigo( entrada.nextInt());

        System.out.println("Peso: ");
        setPeso(entrada.nextDouble());

        System.out.println("Preço: ");
       setPreco(entrada.nextDouble());

        System.out.println("Banda: ");
        setBanda(entrada.next());

        System.out.println("Descrição: ");
        setDescricao(entrada.nextLine());
    }

    public void saida (){

        System.out.println("\n------ Info Produto------");
        System.out.println("Codigo: "+ this.getCodigo());
        System.out.println("Banda: "+ this.getBanda());
        System.out.println("Preço de entrega: " + this.getPeso()* 6.50);
        System.out.println("Preço do produto: "+ this.getPreco());
        System.out.println("Descrição: "+ this.getDescricao());
    }

}
