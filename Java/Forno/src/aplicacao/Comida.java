package aplicacao;

// importará todas as classes do pacote

import assadores.*;

public class Comida {

public static void main(String[] args) {

// TODO Auto-generated method stub

Forno f = new Forno("GE", "f505", 60, 120);

Microondas m = new Microondas("Brastemp", "M328", 28, 250);

f.assar(200);

f.desligar();

m.aquecer(150);

m.desligar();

}

}