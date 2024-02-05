class Rational:
    def __init__(self, num=0, den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self):
        if self.numerator == 0 and self.denominator >= 0:
            return "0"
        elif self.numerator > 1 and self.denominator == 1:
            return str(self.numerator//self.denominator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)
    def scale(self, num):
        self.numerator *= num
        self.denominator *= num
        
num1 = Rational(3,4)
num2 = Rational(1,3)
num3 = Rational(4,1)
num4 = Rational(0/4)
num1.scale(3)
print(num1)
print(num2)
print(num3)
print(num4)

    
