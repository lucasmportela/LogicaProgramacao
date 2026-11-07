package biblioteca;

import java.util.Scanner;

public class Forno implements Controle {

private String marca, modelo;

private int volume, potencia;

public String getMarca() {

return marca;

}

public void setMarca( String marca ) {

this.marca = marca;

}

public String getModelo() {

return modelo;

}

public void setModelo( String modelo ) {

this.modelo = modelo;

}

public int getVolume() {

return volume;

}

public void setVolume( int volume ) {

this.volume = volume;

}

public int getPotencia() {

return potencia;

}

public void setPotencia( int potencia ) {

this.potencia = potencia;

}

public Forno( ) { }

public Forno( String marca, String modelo ) {

this.marca = marca;

this.modelo = modelo;

}

public Forno( int volume, int potencia ) {

this.volume = volume;

this.potencia = potencia;

}

public Forno( String marca, String modelo, int volume, int potencia ) {

this.marca = marca;

this.modelo = modelo;

this.volume = volume;

this.potencia = potencia;

}

public void cadastrar( String marca, String modelo, int volume, int potencia ) {

this.marca = marca;

this.modelo = modelo;

this.volume = volume;

this.potencia = potencia;

}

public void imprimir() {

System.out.println("\nMarca :" + getMarca());

System.out.println("Modelo :" + getModelo());

System.out.println("Volume :" + getVolume());

System.out.println("Potência:" + getPotencia());

}

public void entrada() {

Scanner ent = new Scanner(System.in);

System.out.println("\nMarca :");

setMarca(ent.nextLine());

System.out.println("Modelo :");

setModelo(ent.nextLine());

System.out.println("Volume :");

setVolume(Integer.parseInt(ent.nextLine()));

System.out.println("Potência:");

setPotencia(Integer.parseInt(ent.nextLine()));

}

public int getPotenciaMaxima() {

return POTENCIAMAXIMA;

}

public int getPotenciaMinima() {

return POTENCIAMINIMA;

}

public void assar(int potencia) {

setPotencia(potencia);

System.out.println("\nForno assando com potencia=" + getPotencia());

}

public void aquecer(int potencia) {

setPotencia(potencia);

System.out.println("\nForno aquecendo com potencia=" + getPotencia());

}

public void desligar() {

System.out.println("\nDesligar Forno.");

}

}