public class AppAgregacao {
    public static void main(String[] args) {
    // TODO Auto-generated method stub
    Desktop desk = new Desktop();
    desk.entradaDados();
    desk.imprimir();
    Notebook note = new Notebook();
    note.entradaDados();
    note.imprimir();
    Servidor server = new Servidor();
    server.entradaDados();
    server.imprimir();
    }
}