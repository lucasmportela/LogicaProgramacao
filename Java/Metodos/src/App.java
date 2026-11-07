public class App {
    public static void main(String[] args) throws Exception {
        Caneta c1 = new Caneta("Bic", "Vermelha", 0.5f, 90, false);
        c1.status();

        Caneta c2 = new Caneta("Compactor", "Preta", 0.7f, 100, true);
        c2.status();

        Caneta c3 = new Caneta("Cis", "Azul", 1f, 0, false);
        c3.status();


    }
}
