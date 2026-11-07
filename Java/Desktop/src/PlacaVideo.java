import java.util.Scanner;
public class PlacaVideo {
 public String marca, modelo;
 public double preco;
 public int capacidade;
 public PlacaVideo( ) { }
 public PlacaVideo( String ma, String mo ) {
setMarca( ma );
setModelo( mo );
 }
 public PlacaVideo( String ma, String mo, double pr ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
 }
 public PlacaVideo( String ma, String mo, double pr, int ca ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
setCapacidade( ca );
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
public double getPreco() {
return preco;
}
public void setPreco( double pr ) {
if( pr>0 ) {
preco = pr;
}
}
public int getCapacidade() {
return capacidade;
}
public void setCapacidade( int ca ) {
if( ca>0 ) {
capacidade = ca;
}
}
 public void cadastrar( String ma, String mo, double pr, int ca ) {
setMarca( ma );
setModelo( mo );
setPreco( pr );
setCapacidade( ca );
 }
 public void imprimir( ) {
System.out.println( "Marca :" + getMarca( ));
System.out.println( "Modelo :" + getModelo( ));
System.out.println( "Preço :" + getPreco( ));
System.out.println( "Capacidade :" + getCapacidade( ));
 }
 public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Marca :");
    setMarca( entrada.nextLine( ));
    System.out.println("Modelo :");
    
    setModelo( entrada.nextLine( ));
    System.out.println("Preço :");
    setPreco(Double.parseDouble( entrada.nextLine( )));
    System.out.println("Capacidade :");
    setCapacidade(Integer.parseInt( entrada.nextLine( )));
     }
}
