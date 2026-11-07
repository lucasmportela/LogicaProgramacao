package biblioteca;

import biblioteca.Forno;

public class AppForno {

public static void main(String[] args) {

// TODO Auto-generated method stub

// ojbetos Forno e Microondas

Forno f1 = new Forno(null, null, 0, 0);

f1.entrada();
f1.imprimir();

f1.aquecer(400);

f1.desligar();

f1.assar(450);

}

}