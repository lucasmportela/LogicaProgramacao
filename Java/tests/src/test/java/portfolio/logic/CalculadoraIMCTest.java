package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class CalculadoraIMCTest {
 @Test void calculaImc() { assertEquals(25.0, CalculadoraIMC.calcular(80, 1.8), 0.0001); }
 @Test void rejeitaPesoZero() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(0, 1.7)); }
 @Test void rejeitaAlturaNegativa() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(70, -1.7)); }
 @Test void classificaAbaixoDoPeso() { assertEquals("Abaixo do peso!", CalculadoraIMC.classificar(18.49)); }
 @Test void classificaPesoIdeal() { assertEquals("Peso ideal!", CalculadoraIMC.classificar(18.5)); }
 @Test void classificaSobrepeso() { assertEquals("Sobrepeso!", CalculadoraIMC.classificar(25.0)); }
 @Test void classificaObesidade() { assertEquals("Obesidade!", CalculadoraIMC.classificar(30.0)); }
 @Test void classificaObesidadeGrave() { assertEquals("Obesidade grave!", CalculadoraIMC.classificar(40.0)); }
}
