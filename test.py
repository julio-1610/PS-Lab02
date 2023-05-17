import unittest
from atm_simple import Cajero

class retirarTest(unittest.TestCase):
  def test_retirar_correcto(self):
    cajero = Cajero()
    self.assertEqual(cajero.retirarTEST(2000), 3000)
    
  def test_retirar_monto_mayor(self):
    cajero = Cajero()
    self.assertEqual(cajero.retirarTEST(5000), 0)
    
  def test_retirar_monto_negativo(self):
    cajero = Cajero()
    self.assertEqual(cajero.retirarTEST(-2000), -1)

class depositarTest(unittest.TestCase):
  def test_depositar_correcto(self):
    cajero = Cajero()
    self.assertEqual(cajero.depositarTEST(2000), 7000)
  
  def test_depositar_monto_mayor(self):
    cajero = Cajero()
    self.assertEqual(cajero.depositarTEST(5001), -1)
  
  def test_depositar_monto_negativo(self):
    cajero = Cajero()
    self.assertEqual(cajero.depositarTEST(-2000), -1)
  
class verTest(unittest.TestCase):
  def test_ver_correcto(self):
    cajero = Cajero()
    self.assertEqual(cajero.verTEST(), 5000)
    
#unittest.main()
if __name__=='__main__':
    unittest.main()

