public class App {
    public static void main(String[] args) throws Exception {
        Caneta c1 = new Caneta();
        c1.cor = "vermelha";
        c1.ponta = 0.7f;
        c1.modelo = "bic";
        c1.carga = 90;
        c1.destampar();
        c1.status();
        c1.rabiscar();
        
        Caneta c2 = new Caneta();
        c2.cor = "azul";
        c2.ponta = 0.5f;
        c2.modelo = "compactor";
        c2.carga = 1;
        c2.tampar();
        c2.status();
        c2.rabiscar();

        
    }
}
