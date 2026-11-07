import java.util.Scanner;
public class HD {
public String marca, modelo, tipo;
public double preco;
public int capacidade;
public HD( ) { }
public HD( String ma, String mo ) {
setMarca( ma );
setModelo( mo );
}
public HD( String ma, String mo, String ti ) {
setMarca( ma );
setModelo( mo );
setTipo( ti );
}
public HD( String ma, String mo, String ti, double pr ) {
setMarca( ma );
setModelo( mo );
setTipo( ti );
setPreco( pr );
}
public HD( String ma, String mo, String ti, double pr, int ca ) {
setMarca( ma );
setModelo( mo );
setTipo( ti );
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
public String getTipo() {
return tipo;
}
public void setTipo( String ti ) {
if( !ti.isEmpty() ) {
tipo = ti;
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
public void setCapacidade(int ca) {
if( ca>0 ) {
capacidade = ca;
}
}
public void cadastrar( String ma, String mo, String ti, double pr, int ca ){
setMarca( ma );
setModelo( mo );
setTipo( ti );
setPreco( pr );
setCapacidade( ca );
}
public void imprimir( ) {
System.out.println( "Marca :" + getMarca( ));
System.out.println( "Modelo :" + getModelo( ));
System.out.println( "Processador :" + getTipo( ));
System.out.println( "Preço :" + getPreco( ));
System.out.println( "Capacidade :" + getCapacidade( ));
}
public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Marca :");
    setMarca( entrada.nextLine( ));
    System.out.println("Modelo :");
    setModelo( entrada.nextLine( ));
    System.out.println("Tipo :");
    setTipo( entrada.nextLine( ));
    System.out.println("Preço :");
    setPreco(Double.parseDouble( entrada.nextLine( )));
    System.out.println("Capacidade :");
    setCapacidade(Integer.parseInt( entrada.nextLine( )));
    }
}
    