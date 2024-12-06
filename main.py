from fraction import Fraction
import unittest


fraction1 = Fraction(15,8)
fraction2 = Fraction(0,6)
fraction3 = Fraction(84,12)


class Fract_test(unittest.TestCase):
    def test_fraction_den_positif(self):
        """Vérification du calcul de la fraction dans le cas den>0"""
        self.assertEqual(fraction1-fraction2, Fraction(15,8),"f1 - f2")
        self.assertEqual(fraction2.is_zero(), True, "f2 is 0")
        self.assertEqual(fraction1 + fraction3, Fraction(71,8), "f1+f3")

    def test_fraction_den_zero(self):
        """Vérification de la positivité du denominateur"""
        self.assertRaises(AssertionError,Fraction,15,0)

    def test_fraction_not_int(self):
        """Vérification de la génération d'une exception en cas d'appel sur un nombre négatif"""
        self.assertRaises(TypeError, Fraction, None,True)
        self.assertRaises(TypeError, Fraction, 'huit',[15,23])

