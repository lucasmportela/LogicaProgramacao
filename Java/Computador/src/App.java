public class App {
    public static void main(String[] args) throws Exception {
        // Uma loja vende 3 tipos de produto: livro, CD e software. Para todos os produtosexiste
        // código, descrição, preço e peso. Para o CD existe o nome da banda, para o livro existe o
        // nome do autor e para o software existe a categoria. Para entregar um produto, o cálculo
        // do frete é feito multiplicando o peso do produto por R$ 6,50. Implemente as classes que
        // retratam esse cenário.

        CD c1 = new CD(0, null, 0, 0, null);
        c1.entrada();
        c1.saida();

    }
}

