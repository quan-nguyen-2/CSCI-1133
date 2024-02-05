class Poly:
    def __init__(self, coefficients=[0]):
        self.coefficients = coefficients

    def degree(self):
        for i in range(len(self.coefficients)-1, 0, -1):
            if not self.coefficients[i] == 0:
                return self.coefficients[i]

    def insertTerm(self, coefficient, term):
        if term > len(self.coefficients):
            for i in range((term-len(self.coefficients)-1)):
                self.coefficients.append(0)
            self.coefficients.append(coefficient)
        else:
            self.coefficients[term] += coefficient

    def __str__(self):
        ret = ""
        for i in range(len(self.coefficients)):
            if i == 0:
                ret = " + " + str(self.coeffients[i]) + ret

            elif i == 1:
                ret = " + " + str(self.coefficients[i]) + "x" + ret

            elif i == len(self.coefficients) - 1:

                if self.coefficients[i] == 1:
                    ret = "x" + str[i] + ret
                else:
                    ret = str(self.coeffcients[i]) + "x" + str[i] + ret
            else:
                if self.coefficients[i] == 1:
                    ret = " + " + "x" + str[i] + ret
                else:
                    ret = " + " + str(self.coefficients[i]) + "x" + str(i) + ret
        if ret == "":
            return str(0)
        else:
            return ret
    
    def integrate(self):
        for i in range(len(self.coefficients)):
            self.coefficients[i] = self.coefficients[i] + "/" + str(i+1)
        self.coefficients = [0] + self.coefficients
        
num1 = Poly([3, 2, 1])
print(num1)
        
        
        


        
