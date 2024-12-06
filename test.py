from fraction import Fraction
import unittest


fraction1 = Fraction(1,8)
fraction2 = Fraction(0,6)
fraction3 = Fraction(40,10)
fraction4 = Fraction(5,3)
fraction5 = Fraction(2,3)


class Fract_test(unittest.TestCase):
    def test_fraction_constructeur(self):
        self.assertEqual(fraction1.numerator,1)
        self.assertEqual(fraction1.denominator,8)
        self.assertRaises(AssertionError,Fraction,2,0)

    def test_print(self):
        self.assertEqual(str(fraction1),"1 / 8")

    def test_mixed_number(self):
        self.assertEqual(fraction3.as_mixed_number(),"4")
        self.assertEqual(Fraction(8,5).as_mixed_number(),'1 3/5')

    def test_fraction_addition(self):
        self.assertEqual(fraction1 + fraction2,Fraction(1,8))

    def test_fraction_subtraction(self):
        self.assertEqual(fraction1 - fraction2,Fraction(1,8))

    def test_fraction_multiplication(self):
        self.assertEqual(fraction3 * fraction1,Fraction(40,80))

    def test_fraction_division(self):
        self.assertEqual(fraction2 / fraction1,Fraction(0,6))

    def test_fraction_power(self):
        self.assertEqual(fraction1 ** Fraction(2,1),Fraction(1,64))

    def test_fraction_equal(self):
        self.assertEqual(fraction1 == Fraction(1,8),True)

    def test_float(self):
        self.assertEqual(float(fraction1),0.125)

    def test_zero(self):
        self.assertEqual(Fraction(0,8).is_zero(),True)
        self.assertEqual(fraction1.is_zero(),False)

    def test_integer(self):
        self.assertEqual(fraction1.is_integer(),False)
        self.assertEqual(Fraction(4,2).is_integer(),True)

    def test_proper(self):
        self.assertEqual(fraction1.is_proper(),True)

    def test_adjacent(self):
        self.assertEqual(fraction4.is_adjacent_to(fraction5),True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
