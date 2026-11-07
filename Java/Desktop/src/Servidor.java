import java.util.Scanner;
 public class Servidor {
 // atributos da classe
 public int numeroPlacasRede;
 // atributos agregados
 public PlacaMae pm = new PlacaMae();
 public PlacaVideo pv = new PlacaVideo();
 public HD hd = new HD();
 public Memoria me = new Memoria();
 public Servidor( ) { }

public Servidor( int npr, PlacaMae pm ) {
setNumeroPlacasRede ( npr );
setPm( pm );
 }
 public Servidor( int npr, PlacaMae pm, PlacaVideo pv ) {
setNumeroPlacasRede ( npr );
setPm( pm );
setPv( pv );
 }
 public Servidor( int npr, PlacaMae pm, PlacaVideo pv, HD hd ) {
setNumeroPlacasRede ( npr );
setPm( pm );
setPv( pv );
setHd( hd );
 }
public Servidor( int npr, PlacaMae pm, PlacaVideo pv, HD hd, Memoria
me ) {
setNumeroPlacasRede ( npr );
setPm( pm );
setPv( pv );
setHd( hd );
setMe( me );
 }
 public int getNumeroPlacasRede() {
return numeroPlacasRede;
 }
 public void setNumeroPlacasRede( int npr ) {
if(npr>0) {
numeroPlacasRede = npr;
}
 }
 public PlacaMae getPm() {
return pm;
 }
 public void setPm( PlacaMae pm ) {
setPm( pm );
 }
 public PlacaVideo getPv() {
return pv;
 }
 public void setPv( PlacaVideo pv ) {
setPv( pv );
 }
 public HD getHd() {
return hd;
 }
 public void setHd( HD hd ) {
setHd( hd );
 }
 public Memoria getMe() {
return me;
 }
 public void setMe( Memoria me ) {
setMe( me );
 }
 public void cadastrar( int npr, PlacaMae pm, PlacaVideo pv,
 HD hd, Memoria me ) {
setNumeroPlacasRede ( npr );
setPm( pm );
setPv( pv );
setHd( hd );
setMe( me );
 }
 public void imprimir( ) {
System.out.println("Servidor--------------------------------");
System.out.println("Número Placas de Rede:" +
getNumeroPlacasRede());
pm.imprimir();
pv.imprimir();
hd.imprimir();
me.imprimir();
 }
 public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Servidor--------------------------------");
    System.out.println("Número Placas de Rede:");
    setNumeroPlacasRede( Integer.parseInt( entrada.nextLine( )));
    pm.entradaDados();
    pv.entradaDados();
    hd.entradaDados();
    me.entradaDados();
     }
}
    