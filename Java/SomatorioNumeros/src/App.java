public class App {
    public static void main(String[] args) throws Exception {
        //Escreva um programa em Java que leia números inteiros positivos e imprima o
        //somatório desses números. O programa deve parar de ler quando o usuário digitar um
        //número menor ou igual a zero. Faça o tratamento de exceção para o caso do usuário não
        //digitar um número quando solicitado

        Somatorio somatorio = new Somatorio(1, 0);
        somatorio.entrada();

    }
}
