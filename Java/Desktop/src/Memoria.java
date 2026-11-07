import java.util.Scanner;
public class Memoria {
public String marca, modelo, padrao;
public double preco;
public Memoria( ) { }
public Memoria( String ma, String mo ) {
setMarca( ma );
setModelo( mo );
}
public Memoria( String ma, String mo, double pr ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
}
public Memoria( String ma, String mo, double pr, String pa ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
setPadrao( pa );
}
public String getMarca() {
return marca;
}
public void setMarca( String ma ) {
if(!ma.isEmpty()) {
marca = ma;
}
}
public String getModelo() {
return modelo;
}
public void setModelo( String mo ) {
if(!mo.isEmpty()) {
modelo = mo;
}
}
public double getPreco() {
return preco;
}
public void setPreco( double pr ) {
if(pr>0) {
preco = pr;
}
}
public String getPadrao() {
return padrao;
}
public void setPadrao( String pa ) {
if(!pa.isEmpty()) {
padrao = pa;
}
}
public void cadastrar( String ma, String mo, double pr, String pa ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
setPadrao( pa );
}
public void imprimir( ) {
System.out.println( "Marca :" + getMarca( ));
System.out.println( "Modelo :" + getModelo( ));
System.out.println( "Preço :" + getPreco( ));
System.out.println( "Padrão :" + getPadrao( ));
}
public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Marca :");
    setMarca( entrada.nextLine( ));
    System.out.println("Modelo :");
    setModelo( entrada.nextLine( ));
    System.out.println("Preço :");
    setPreco(Double.parseDouble( entrada.nextLine( )));
    System.out.println("Padrão :");
    setPadrao( entrada.nextLine( ));
    }
}
    