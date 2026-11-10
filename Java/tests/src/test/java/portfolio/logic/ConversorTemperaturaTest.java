package portfolio.logic;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
class ConversorTemperaturaTest {
 @Test void converteZeroCelsius() { assertEquals(32.0, ConversorTemperatura.celsiusParaFahrenheit(0), 0.0001); }
 @Test void converteCemCelsius() { assertEquals(212.0, ConversorTemperatura.celsiusParaFahrenheit(100), 0.0001); }
 @Test void converteTemperaturaNegativa() { assertEquals(-40.0, ConversorTemperatura.celsiusParaFahrenheit(-40), 0.0001); }
}
