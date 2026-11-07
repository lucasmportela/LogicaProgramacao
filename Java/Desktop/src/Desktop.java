import java.util.Scanner;
public class Desktop {
// atributos da classe
public String tipoCooler;
// atributos agregados
 public PlacaMae pm = new PlacaMae();
 public PlacaVideo pv = new PlacaVideo();
 public HD hd = new HD();
 public Memoria slot0 = new Memoria();
 public Memoria slot1 = new Memoria();
 public Desktop( ) {}
 public Desktop( String tc, PlacaMae pm ) {
setTipoCooler( tc );
setPm (pm );
 }
 public Desktop( String tc, PlacaMae pm, PlacaVideo pv ) {
setTipoCooler( tc );
setPm (pm );
setPv( pv );
 }
 public Desktop( String tc, PlacaMae pm, PlacaVideo pv, HD hd ) {
setTipoCooler( tc );
setPm (pm );
setPv( pv );
setHd( hd );
 }
 public Desktop( String tc, PlacaMae pm, PlacaVideo pv, HD hd,
 Memoria slot0, Memoria slot1 ) {
setTipoCooler( tc );
setPm (pm );
setPv( pv );
setHd( hd );
setSlot0( slot0 );
setSlot1( slot1 );
 }
 public String getTipoCooler() {
return tipoCooler;
 }
 public void setTipoCooler( String tc ) {
if(!tc.isEmpty()) {
tipoCooler = tc;
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
 public void setHd(HD hdp) {
hd = hdp;
 }
 public Memoria getSlot0() {
return slot0;
 }
 public void setSlot0( Memoria sl0 ) {
slot0 = sl0;
 }
 public Memoria getSlot1() {
return slot1;
 }
 public void setSlot1( Memoria sl1 ) {
slot1 = sl1;
 }
 public void cadastrar( String tc, PlacaMae pm, PlacaVideo pv, HD hd,
 Memoria slot0, Memoria slot1 ) {
setTipoCooler( tc );
setPm (pm );
setPv( pv );
setHd( hd );
setSlot0( slot0 );
setSlot1( slot1 );
 }
 public void imprimir( ) {
System.out.println("Desktop---------------------------------");
System.out.println("tipo Cooler :" + getTipoCooler( ));
pm.imprimir();
pv.imprimir();
hd.imprimir();
slot0.imprimir();
slot1.imprimir();
 }
 public void entradaDados( ) {
    Scanner entrada = new Scanner( System.in );
    System.out.println("Desktop---------------------------------");
    System.out.println("tipo Cooler :");
    setTipoCooler( entrada.nextLine( ));
    pm.entradaDados();
    pv.entradaDados();
    hd.entradaDados();
    slot0.entradaDados();
    slot1.entradaDados();
     }
    }
