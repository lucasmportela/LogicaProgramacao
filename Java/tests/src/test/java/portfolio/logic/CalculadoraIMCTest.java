package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class CalculadoraIMCTest {
 @Test void calculaImc() { assertEquals(24.691358, CalculadoraIMC.calcular(80, 1.8), 0.0001); }
 @Test void rejeitaPesoZero() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(0, 1.7)); }
 @Test void rejeitaAlturaNegativa() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(70, -1.7)); }
 @Test void rejeitaPesoNaoFinito() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(Double.NaN, 1.7)); assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(Double.POSITIVE_INFINITY, 1.7)); }
 @Test void rejeitaAlturaNaoFinita() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(70, Double.NaN)); assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.calcular(70, Double.POSITIVE_INFINITY)); }
 @Test void rejeitaClassificacaoDeImcInvalido() { assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.classificar(-1)); assertThrows(IllegalArgumentException.class, () -> CalculadoraIMC.classificar(Double.NaN)); }
 @Test void classificaAbaixoDoPeso() { assertEquals("Abaixo do peso!", CalculadoraIMC.classificar(18.49)); }
 @Test void classificaPesoIdeal() { assertEquals("Peso ideal!", CalculadoraIMC.classificar(18.5)); }
 @Test void classificaSobrepeso() { assertEquals("Sobrepeso!", CalculadoraIMC.classificar(25.0)); }
 @Test void classificaObesidade() { assertEquals("Obesidade!", CalculadoraIMC.classificar(30.0)); }
 @Test void classificaObesidadeGrave() { assertEquals("Obesidade grave!", CalculadoraIMC.classificar(40.0)); }
}
