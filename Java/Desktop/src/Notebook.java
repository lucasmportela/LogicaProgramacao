import java.util.Scanner;
public class Notebook {
 // atributos da classe
 public double peso;
 // atributos agregados
 public PlacaMae pm = new PlacaMae();
 public PlacaVideo pv = new PlacaVideo();
 public HD hd = new HD();
 public Memoria me = new Memoria();
 public Notebook( ) { }
 public Notebook( double pe, PlacaMae pm ) {
setPeso( pe );
setPm( pm );
 }
 public Notebook( double pe, PlacaMae pm, PlacaVideo pv ) {
setPeso( pe );
setPm( pm );
setPv( pv );
 }
 public Notebook( double pe, PlacaMae pm, PlacaVideo pv, HD hd ) {
setPeso( pe );
setPm( pm );
setPv( pv );
setHd( hd );
 }
 public Notebook(double pe, PlacaMae pm, PlacaVideo pv, HD hd,
Memoria me){
setPeso( pe );
setPm( pm );
setPv( pv );
setHd( hd );
setMe( me );
 }
 public double getPeso() {
return peso;
 }
 public void setPeso( double pe ) {
if(pe>0) {
peso = pe;
}
 }
 public PlacaMae getPm() {
return pm;
 }
 public void setPm( PlacaMae pmp ) {
pm = pmp;
 }
 public PlacaVideo getPv() {
return pv;
 }
 public void setPv( PlacaVideo pvp ) {
pv = pvp;
 }
 public HD getHd() {
return hd;
 }
 public void setHd( HD hdp ) {
hd = hdp;
 }
 public Memoria getMe() {
return me;
 }
 public void setMe( Memoria mep ) {
me = mep;
 }
 public void cadastrar( double pe, PlacaMae pm, PlacaVideo pv,
 HD hd, Memoria me ) {
setPeso( pe );
setPm( pm );
setPv( pv );
setHd( hd );
setMe( me );
 }
 public void imprimir( ) {
System.out.println("Notebook--------------------------------");
System.out.println("Peso :" + getPeso( ));
pm.imprimir();
pv.imprimir();
hd.imprimir();
me.imprimir();
 }
public void entradaDados( ) {
Scanner entrada = new Scanner( System.in );

System.out.println("Notebook--------------------------------");
System.out.println("Peso :");
setPeso( Double.parseDouble(entrada.nextLine( )));
pm.entradaDados();
pv.entradaDados();
hd.entradaDados();
me.entradaDados();
}
}
