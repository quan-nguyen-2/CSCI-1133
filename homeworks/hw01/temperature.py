# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# temperature

def convertToCelsius(fahrenheit):
    Celsius = (5/9*(fahrenheit - 32))
    return Celsius
result = convertToCelsius(32)

# C = Celcius and f = fahrenheit
def convertTofahrenheit(C):
    F = (32+(C * 9/5))
    return F
result2 = convertTofahrenheit(40)

print("Celsius:", result)
print("Fahrenheit:", result2)
