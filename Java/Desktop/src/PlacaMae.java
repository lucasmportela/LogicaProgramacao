import java.util.Scanner;
public class PlacaMae {
 public String marca, modelo, tipoProcessador;
 public double preco;
 public PlacaMae() { }
 public PlacaMae( String ma, String mo ) {
setMarca( ma );
setModelo( mo );
 }
 public PlacaMae( String ma, String mo, String tp ) {
setMarca( ma );
setModelo( mo );
setTipoProcessador( tp );
 }
 public PlacaMae( String ma, String mo, String tp, double pr ) {
setMarca( ma );
setModelo( mo );
setTipoProcessador( tp );
setPreco( pr );
 }
 public String getMarca() {
return marca;
 }
 public void setMarca( String ma ) {
if( !ma.isEmpty() ) {
marca = ma;
}
 }
 public String getModelo() {
return modelo;
 }
 public void setModelo( String mo ) {
if( !mo.isEmpty() ) {
modelo = mo;
}
 }
 public String getTipoProcessador() {
return tipoProcessador;
 }
 public void setTipoProcessador( String tp ) {
if( !tp.isEmpty() ) {
tipoProcessador = tp;
}
 }
 public double getPreco() {
return preco;
 }
 public void setPreco(double pr) {
if( pr>0 ) {
preco = pr;
}
 }
 public void cadastrar ( String ma, String mo, String tp, double pr ) {
setMarca( ma );
setModelo( mo );
setTipoProcessador( tp );
setPreco( pr );
 }
 public void imprimir( ) {
System.out.println( "Marca :" + getMarca( ));
System.out.println( "Modelo :" + getModelo( ));
System.out.println( "Processador :" + getTipoProcessador( ));
System.out.println( "Preço :" + getPreco( ));
 }
 public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Marca :");
    setMarca( entrada.nextLine( ));
    System.out.println("Modelo :");
    setModelo( entrada.nextLine( ));
    System.out.println("Processador :");
    setTipoProcessador( entrada.nextLine( ));
    System.out.println("Preço :");
    setPreco(Double.parseDouble( entrada.nextLine( )));
     }
    }
    