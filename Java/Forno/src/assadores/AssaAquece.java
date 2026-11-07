package assadores;

import java.util.Scanner;

public abstract class AssaAquece {

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

public AssaAquece( ) { }

public AssaAquece( String marca, String modelo ) {

this.marca = marca;

this.modelo = modelo;

}

public AssaAquece( int volume, int potencia ) {

this.volume = volume;

this.potencia = potencia;

}

public AssaAquece( String marca, String modelo, int volume, int potencia ) {

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

System.out.println("Marca :" + getMarca());

System.out.println("Modelo :" + getModelo());

System.out.println("Volume :" + getVolume());

System.out.println("Potência:" + getVolume());

}

public void entrada() {

Scanner ent = new Scanner(System.in);

System.out.println("Marca :");

setMarca(ent.nextLine());

System.out.println("Modelo :");

setModelo(ent.nextLine());

System.out.println("Volume :");

setVolume(Integer.parseInt(ent.nextLine()));

System.out.println("Potência:");

setVolume(Integer.parseInt(ent.nextLine()));

}

public abstract void assar(int potencia);

public abstract void aquecer(int potencia);

public abstract void desligar();

}