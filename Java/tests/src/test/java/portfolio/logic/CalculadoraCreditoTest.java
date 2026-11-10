package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class CalculadoraCreditoTest {
 @Test void saldoAteDoisMilNaoGeraCredito() { assertEquals(0.0, CalculadoraCredito.calcularCredito(2000), 0.0001); }
 @Test void aplicaVintePorCento() { assertEquals(400.002, CalculadoraCredito.calcularCredito(2000.01), 0.0001); assertEquals(800.0, CalculadoraCredito.calcularCredito(4000), 0.0001); }
 @Test void aplicaTrintaPorCento() { assertEquals(1200.003, CalculadoraCredito.calcularCredito(4000.01), 0.0001); assertEquals(1800.0, CalculadoraCredito.calcularCredito(6000), 0.0001); }
 @Test void aplicaQuarentaPorCento() { assertEquals(2400.4, CalculadoraCredito.calcularCredito(6001), 0.0001); }
 @Test void rejeitaSaldoNegativo() { assertThrows(IllegalArgumentException.class, () -> CalculadoraCredito.calcularCredito(-1)); }
 @Test void rejeitaSaldoNaoFinito() { assertThrows(IllegalArgumentException.class, () -> CalculadoraCredito.calcularCredito(Double.NaN)); assertThrows(IllegalArgumentException.class, () -> CalculadoraCredito.calcularCredito(Double.POSITIVE_INFINITY)); assertThrows(IllegalArgumentException.class, () -> CalculadoraCredito.calcularCredito(Double.NEGATIVE_INFINITY)); }
}
