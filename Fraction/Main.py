import math
import Fraction

frac_pi = Fraction.Fraction(math.pi)
frac_a = Fraction.Fraction(2,3) + Fraction.Fraction(5,2) * Fraction.Fraction(6,15) - Fraction.Fraction(3,2)
frac_b = Fraction.Fraction(2/3 + 5/2 * 6/15 - 3/2)

print("frac_pi", frac_pi)
print()
print("frac_a", frac_a)
print("frac_b", frac_b)
print("frac_a == frac_b ?")
print(frac_a == frac_b)

#output pause
input()