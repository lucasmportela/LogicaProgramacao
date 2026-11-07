package assadores;

import java.util.Scanner;

public class Microondas extends AssaAquece{

public Microondas( ) {

super();

}

public Microondas( String marca, String modelo ) {

super(marca, modelo);

}

public Microondas( int volume, int potencia ) {

super(volume, potencia);

}

public Microondas( String marca, String modelo, int volume, int potencia ) {

super(marca, modelo, volume, potencia);

}

public void cadastrar( String marca, String modelo, int volume, int potencia ) {

super.cadastrar(marca, modelo, volume, potencia);

}

public void imprimir() {

super.imprimir();

}

public void entrada() {

super.entrada();

}

private void girar(boolean giro) {

if(giro){

System.out.println("Girando o prato!");

}

else {

System.out.println("Prato parado!");

}

}

public void assar(int potencia) {

super.setPotencia(potencia);

girar(true);

System.out.println("Microondas assando com potencia=" + super.getPotencia());

}

public void aquecer(int potencia) {

super.setPotencia(potencia);

girar(true);

System.out.println("Microondas aquecendo com potencia=" +

super.getPotencia());

}

public void desligar() {

girar(false);

System.out.println("Desligar Microondas");

}

}