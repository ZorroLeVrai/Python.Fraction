import math

epsilon = 1e-5

#Class to make operations on Fractions
class Fraction:

    #initialize the class
    def __init__(self, *args):
        if len(args) > 1:
            self.init_num_denum(args[0], args[1])
        else:
            self.init_number(args[0])

    #tostring function
    def __str__(self):
        return "{0}/{1}".format(int(self.numerator), int(self.denominator))

    #summing 2 fractions (+ operator)
    def __add__(self, other):
        common_den = self.denominator * other.denominator
        num = self.numerator * other.denominator + other.numerator * self.denominator
        denum = common_den
        common_div = math.gcd(num, denum)
        return Fraction(num // common_div, denum // common_div)

    #subtracting 2 fractions (- operator)
    def __sub__(self, other):
        common_den = self.denominator * other.denominator
        num = self.numerator * other.denominator - other.numerator * self.denominator
        denum = common_den
        common_div = math.gcd(num, denum)
        return Fraction(num // common_div, denum // common_div)

    #multiplying 2 fractions (* operator)
    def __mul__(self, other):
        num = self.numerator * other.numerator
        denum = self.denominator * other.denominator
        common_div = math.gcd(num, denum)
        return Fraction(num // common_div, denum // common_div)

    #dividing 2 fractions (/ operator)
    def __truediv__(self, other):
        inv_other = Fraction.get_invert(other);
        return self.__mul__(inv_other)

    #equality operator
    def __eq__(self, other):
        return (self.numerator / self.denominator) == (other.numerator / other.denominator)

    #inequality operator
    def __ne__(self, other):
        return (self.numerator / self.denominator) != (other.numerator / other.denominator)

    #less than operator
    def __lt__(self, other):
        return (self.numerator / self.denominator) < (other.numerator / other.denominator)

    #less or equal operator
    def __le__(self, other):
        return (self.numerator / self.denominator) <= (other.numerator / other.denominator)

    #greater than operator
    def __gt__(self, other):
        return (self.numerator / self.denominator) > (other.numerator / other.denominator)

    #greater or equal operator
    def __ge__(self, other):
        return (self.numerator / self.denominator) >= (other.numerator / other.denominator)

    #get the invert of a given fraction
    def get_invert(other):
        return Fraction(other.denominator, self.denominator)

    #init the Fraction using a number
    #tries to get the closest fraction to the given number
    def init_number(self, number):
        decimal, whole = math.modf(number)
        if decimal < epsilon:
            self.numerator = whole
            self.denominator = 1
        elif decimal > 1 - epsilon:
            self.numerator = whole + 1
            self.denominator = 1
        else:
            num, denum = self.__set_decimal_number_rec(whole, decimal, epsilon)
            self.numerator = num
            self.denominator = denum

    #init the Fraction using 2 a numerator and denominator
    def init_num_denum(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    #used to find the closest numerator and denominator that match the value whole + decimal
    #whole: the integer part of the number
    #decimal: the float part of the number
    #delta_max: delta max to consider before stoping the computing
    #return numerator, denominator that match the value whole + decimal
    def __set_decimal_number_rec(self, whole, decimal, delta_max):
        if decimal < delta_max:
            return whole, 1
        elif decimal > 1 - delta_max:
            return whole + 1, 1
        else:
            #try to rationalize the invert of the decimal part
            invert = 1/decimal
            inv_decimal, inv_whole = math.modf(invert)
            #multiply the delta max by inv_whole
            num, denum = self.__set_decimal_number_rec(inv_whole, inv_decimal, delta_max * inv_whole)
            return num * whole + denum, num

#Factorization class. It is used to factorize the given integer
class Factorization:
    #init the class with an integer
    def __init__(self, int_num):
        self.factors = self.factorize(int_num)

    #tostring function
    def __str__(self):
        to_print = ""
        for key, val in self.factors:
            if 0 < len(to_print):
                to_print += " "
            if val > 1:
                to_print += "{0}^{1}".format(int(key), val)
            else:
                to_print += "{0}".format(int(key))
        return to_print

    #return a dictionary of factors in the following format
    #{ k1:v1, k2:v2, ... } where int_enum = k1**v1 + k2**v2 + ...
    def factorize(self, int_enum):
        return self.__factorize_rec(int(int_enum))

    #return a dictionary of factors using a recursive function
    #the following format { k1:v1, k2:v2, ... } is returned
    #where int_enum = k1**v1 + k2**v2 + ...
    def __factorize_rec(self, int_enum):
        div = 2;
        while (div*div <= int_enum):
            if (0 == int_enum % div):
                return self.__add_element(self.__factorize_rec(int_enum // div), div)
            else:
                div += 1
        if (int_enum > 1):
            return { int_enum:1 }
        else:
            return dict()

    #add element 'elem' in the factorization dico 'factorization_dico'
    def __add_element(self, factorization_dico, elem):
        if elem in factorization_dico:
            factorization_dico[elem] += 1
        else:
            factorization_dico[elem] = 1
        return factorization_dico
