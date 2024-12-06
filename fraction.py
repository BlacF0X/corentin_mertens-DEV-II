from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den are PRIVATE INT. Den != 0
        POST : cree une fraction basée sur le numérateur et le dénominateur
        """
        assert den != 0,'den must be different from 0'
        self.__num = num
        self.__den = den
        try:
            self.__res = self.__num/self.__den
        except TypeError:
            raise TypeError("one of the argument isn't an integer")



    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : uses the numerator and denominator of the fraction
        POST : returns a string representation of the reduced form of the fraction
        """
        if self.__den == 0:
            return "division by zero is impossible"
        else:
            if self.__num/self.__den >= 1:
                return self.as_mixed_number()
            elif self.__num/self.__den == 0:
                return f"0"
            else:
                fr = self.reduced_form()
                return f"{fr[0]} / {fr[1]}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : uses the fraction
        POST : return a string representation of the reduced form of the fraction as a mixed number
        """
        red_form_num,red_form_den = self.reduced_form()
        main_int = red_form_num // red_form_den
        final_num = red_form_num - (red_form_den*main_int)
        if final_num == 0:
            return f"{main_int}"
        else:
            return f"{main_int} {final_num}/{red_form_den}"

    def reduced_form(self,num = None,den = None):
        """
        return the reduced form of a fraction
        PRE : num and den are INT. Den >= 0
        POST : return two ints, the reduced numerator and reduced denominator
        """
        if num is None:
            num = self.__num
        if den is None:
            den = self.__den
        diviseur = gcd(num, den)
        num_red = self.__num // diviseur
        den_red = self.__den // diviseur
        return num_red, den_red

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Overloading of the + operator for fractions

         PRE : - other is another fraction
         POST : return an addition of the two fractions as a number
         """

        res_num = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        res_den = self.denominator * other.denominator
        fr = Fraction(res_num, res_den).reduced_form()
        return Fraction(fr[0],fr[1])


    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Overloading of the - operator for fractions

        PRE : - other is another fraction
        POST : return a substraction of the two fractions as a number
        """

        if self.denominator != other.denominator:
            first_num = self.numerator * other.denominator
            first_den = self.denominator * other.denominator
            second_num = other.numerator * self.denominator
            fr = Fraction((first_num - second_num), first_den).reduced_form()
        else:
            fr = Fraction(self.numerator - other.numerator, self.denominator).reduced_form()
        return Fraction(fr[0], fr[1])


    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Overloading of the * operator for fractions

        PRE : - other is another fraction
        POST : return a multiplication of the two fractions as a number
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Overloading of the / operator for fractions

        PRE : - over is another fraction
        POST : return a division of the two fractions as a number
        """
        other_frct = Fraction(other.denominator, other.numerator)
        return self * other_frct

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : - over is another fraction
        POST : return a power of a fraction as a number
        """
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")

            # Raising to a fractional power: (num/den)^(a/b)
        num = self.__num ** other.__num
        den = self.__den ** other.__num

        # Taking the b-th root: equivalent to (num/den)^(1/b)
        if other.__den != 1:  # Only take the root if denominator of exponent isn't 1
            num = num ** (1 / other.__den)
            den = den ** (1 / other.__den)
        print(num,den)
        return Fraction(num, den)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Overloading of the == operator for fractions

        PRE : other is another fraction
        POST : compare two fractions

        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):

        """Returns the decimal value of the fraction

        PRE : use the fraction
        POST : return the fraction as a float
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : use the fraction
        POST : return True if a fraction's value is 0'
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : use the fraction
        POST : return True if a fraction is integer
        """
        return (self.numerator / self.denominator) - (self.numerator // self.denominator) == 0.0



    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : use the fraction
        POST : return True if the absolute value of the fraction is < 1
        """
        return abs(self.numerator /self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : use the numerator of the fraction
        POST : check if the fraction's numerator is 1 in its reduced form
        """
        num,den = self.reduced_form()
        return num == 1

    def is_adjacent_to(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("other must be an instance of Fraction.")
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : other is another fraction
        POST : check if the absolute value of the difference is a unit fraction
        """
        difference = abs(float(self - other))
        return difference % 1 == 0.0

