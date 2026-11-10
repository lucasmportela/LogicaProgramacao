package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class CalculadoraSomatorioTest {
 @Test void acumulaValoresPositivos() { int total=0; total=CalculadoraSomatorio.adicionar(total,5); total=CalculadoraSomatorio.adicionar(total,10); assertEquals(15,total); }
 @Test void rejeitaZeroOuNegativo() { assertThrows(IllegalArgumentException.class, () -> CalculadoraSomatorio.adicionar(10,0)); assertThrows(IllegalArgumentException.class, () -> CalculadoraSomatorio.adicionar(10,-1)); }
 @Test void rejeitaTotalInicialNegativo() { assertThrows(IllegalArgumentException.class, () -> CalculadoraSomatorio.adicionar(-1,5)); }
 @Test void detectaOverflow() { assertThrows(ArithmeticException.class, () -> CalculadoraSomatorio.adicionar(Integer.MAX_VALUE,1)); }
}
