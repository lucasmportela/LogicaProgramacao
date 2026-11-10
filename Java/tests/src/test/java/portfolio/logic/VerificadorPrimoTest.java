package portfolio.logic;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class VerificadorPrimoTest {
 @Test void reconhecePrimos() { assertTrue(VerificadorPrimo.isPrimo(2)); assertTrue(VerificadorPrimo.isPrimo(3)); assertTrue(VerificadorPrimo.isPrimo(97)); }
 @Test void rejeitaMenoresQueDois() { assertFalse(VerificadorPrimo.isPrimo(-7)); assertFalse(VerificadorPrimo.isPrimo(0)); assertFalse(VerificadorPrimo.isPrimo(1)); }
 @Test void rejeitaCompostos() { assertFalse(VerificadorPrimo.isPrimo(4)); assertFalse(VerificadorPrimo.isPrimo(9)); assertFalse(VerificadorPrimo.isPrimo(25)); }
}
