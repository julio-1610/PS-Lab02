import unittest
from atm_simple import Cajero
class cajeroTest(unittest.TestCase):
  def test_retirar_correcto(self):
    cajero = Cajero()
    self.assertEqual(cajero.retirarTEST(2000), 3000)
    
  def test_retirar_monto_mayor(self):
    cajero = Cajero()
    self.assertEqual(cajero.retirarTEST(5000), 0)
    
#unittest.main()
if __name__=='__main__':
    unittest.main()