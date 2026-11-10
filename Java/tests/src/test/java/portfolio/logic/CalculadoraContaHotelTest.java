package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class CalculadoraContaHotelTest {
 @Test void taxaParaMenosDeQuinzeDiarias() { assertEquals(3360.0, CalculadoraContaHotel.calcularTotal(14), 0.0001); }
 @Test void taxaParaQuinzeDiarias() { assertEquals(3300.0, CalculadoraContaHotel.calcularTotal(15), 0.0001); }
 @Test void taxaParaMaisDeQuinzeDiarias() { assertEquals(3440.0, CalculadoraContaHotel.calcularTotal(16), 0.0001); }
 @Test void rejeitaDiariasInvalidas() { assertThrows(IllegalArgumentException.class, () -> CalculadoraContaHotel.calcularTotal(0)); assertThrows(IllegalArgumentException.class, () -> CalculadoraContaHotel.calcularTotal(-2)); }
}
