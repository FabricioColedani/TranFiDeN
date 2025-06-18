import unittest
from logica import convertir_moneda

class TestConversorMoneda(unittest.TestCase):
    def test_conversion_dolar(self):
        resultado, color = convertir_moneda("10", "Dólar")
        self.assertIn("10 Dólar", resultado)
        self.assertIn("ARS", resultado)
        self.assertEqual(color, "#00B894")

    def test_conversion_yen(self):
        resultado, color = convertir_moneda("1000", "Yen")
        self.assertIn("1000 Yen", resultado)
        self.assertIn("ARS", resultado)
        self.assertEqual(color, "#00B894")

    def test_moneda_invalida(self):
        resultado, color = convertir_moneda("10", "💩 Moneda Falsa")
        self.assertTrue(resultado.startswith("Error"))
        self.assertEqual(color, "#FF4D4D")

    def test_monto_invalido(self):
        resultado, color = convertir_moneda("texto", "Dólar")
        self.assertTrue(resultado.startswith("Error"))
        self.assertEqual(color, "#FF4D4D")

if __name__ == "_main_":
    unittest.main()