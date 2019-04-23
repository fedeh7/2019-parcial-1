import unittest
from interfaz_parcial import interfaz
from hexadecimal import conversor

class TestHexadecimal(unittest.TestCase):
    
    def test_interfaz_5(self):
        hexadecimal_number = interfaz(5)
        print("\n En interfaz, El numero ingresado fue 5")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'5')
    
    def test_interfaz_0(self):
        hexadecimal_number = interfaz(0)
        print("\n En interfaz, El numero ingresado fue 0")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'0')
    
    def test_interfaz_50(self):
        hexadecimal_number = interfaz(50)
        print("\n En interfaz, El numero ingresado fue 50")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'32')
    
    def test_interfaz_1519(self):
        hexadecimal_number = interfaz(1519)
        print("\n En interfaz, El numero ingresado fue 1519")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'5EF')
    
    def test_interfaz_4095(self):
        hexadecimal_number = interfaz(4095)
        print("\n En interfaz, El numero ingresado fue 4095")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'FFF')
    
    def test_interfaz_hola(self):
        hexadecimal_number = interfaz("hola")
        print("\n En interfaz, Se ingreso la palabra hola")
        print("Nos tira error: ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'Debe ingresar solo numeros!')
    
    def test_interfaz_string100(self):
        hexadecimal_number = interfaz("100")
        print("\n En interfaz, El numero ingresado fue 100 en string")
        print("Convertido a hexadecimal es ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'64')

    def test_interfaz_15texto15(self):
        hexadecimal_number = interfaz("15texto15")
        print("\n En interfaz, Se ingreso la palabra 15texto15")
        print("Nos tira error: ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'Debe ingresar solo numeros!')
    
    def test_interfaz_vacio(self):
        hexadecimal_number = interfaz("")
        print("\n En interfaz, No se ingreso nada")
        print("Nos tira error: ", hexadecimal_number)
        self.assertEqual(hexadecimal_number,'Debe ingresar solo numeros!')

    
     
if __name__ =='__main__':
    unittest.main()