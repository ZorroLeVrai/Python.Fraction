import math

epsilon = 1e-5

#This is the Fraction class
class Fraction:

    def __init__(self, *args):
        if len(args) > 1:
            self.init_num_denum(args[0], args[1])
        else:
            self.init_number(args[0])

    #constructor with 1 parameter
    def init_number(self, number):
        decimal, whole = math.modf(number)
        if decimal < epsilon:
            self.numerator = whole
            self.denominator = 1
        elif decimal > 1 - epsilon:
            self.numerator = whole + 1
            self.denominator = 1
        else:
            num, denum = self.set_decimal_number_rec(whole, decimal)
            self.numerator = num
            self.denominator = denum

    #constructor with 2 parameters
    def init_num_denum(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    #tostring function
    def __str__(self):
        return "{0}/{1}".format(int(self.numerator), int(self.denominator))

    def set_decimal_number_rec(self, whole, decimal):
        if decimal < epsilon:
            return whole, 1
        elif decimal > 1 - epsilon:
            return whole + 1, 1
        else:
            invert = 1/decimal
            inv_decimal, inv_whole = math.modf(invert)
            num, denum = self.set_decimal_number_rec(inv_whole, inv_decimal)
            return num * whole + denum, num

