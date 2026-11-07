import java.util.Scanner;

 

public class Carro {

// use as regras da boa prática em programação Java

// para os identificadores da classe, dos atributos e dos métodos

String fabricante, modelo, cor, placa;

double valor;

int numeroPortas, anoFabricacao, anoModelo;

public String getFabricante () {

return fabricante;

}

public void setFabricante (String fab) {

if(!fab.isEmpty()) {

fabricante = fab;

}

}

public String getModelo () {

return modelo;

}

public void setModelo (String mod) {

if(!mod.isEmpty()) {

modelo = mod;

}

}

public String getCor () {

return cor;

}

public void setCor (String co) {

if(!co.isEmpty()) {

cor = co;

}

}

public String getPlaca () {

return placa;

}

public void setPlaca (String pla) {

if(!pla.isEmpty()) {

placa = pla;

}

}

public double getValor () {

return valor;

}

public void setValor (double val) {

if(val > 0) {

valor = val;

}

}

public int getNumeroPortas () {

return numeroPortas;

}

public void setNumeroPortas (int nump) {

if(nump > 0) {

numeroPortas = nump;

}

}

public int getAnoFabricacao () {

return anoFabricacao;

}

public void setAnoFabricacao (int anof) {

if(anof > 0) {

anoFabricacao = anof;

}

}

public int getAnoModelo () {

return anoModelo;

}

public void setAnoModelo (int anom) {

if(anom > 0) {

anoModelo = anom;

}

}

public void imprimir (){

System.out.println( "------------------------------------");

System.out.println( "Fabricante : " + getFabricante() );

System.out.println( "Modelo : " + getModelo() );

System.out.println( "Cor : " + getCor() );

System.out.println( "Placa : " + getPlaca() );

System.out.println( "Valor : " + getValor() );

System.out.println( "Número de Portas : " + getNumeroPortas() );

System.out.println( "Ano de fabricação: " + getAnoFabricacao() );

System.out.println( "Ano do Modelo : " + getAnoModelo() );

}

public void entradaDados () {

Scanner entrada = new Scanner( System.in );

// O objeto Scanner deve ficar local ao método

// o objeto Scanner para entrada de dados não é um atributo do carro

// é apenas um objeto auxiliar a entrada de dados

System.out.println("Digite o Fabricante do carro :");

setFabricante( entrada.nextLine() );

System.out.println("Digite o Modelo do carro :");

setModelo( entrada.nextLine() );

System.out.println("Digite a Cor do carro :");

setCor( entrada.nextLine() );

System.out.println("Digite a Placa do carro :");

setPlaca( entrada.nextLine() );

System.out.println("Digite o Valor do carro :");

setValor( Double.parseDouble( entrada.nextLine()) );

System.out.println("Digite o Número de Portas do carro :");

setNumeroPortas( Integer.parseInt( entrada.nextLine()) );

System.out.println("Digite o Ano de fabricação do carro :");

setAnoFabricacao( Integer.parseInt( entrada.nextLine()) );

System.out.println("Digite o Ano do Modelo do carro :");

setAnoModelo( Integer.parseInt( entrada.nextLine()) );

}

}