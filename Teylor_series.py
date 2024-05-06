from math import factorial
def e_power_x(x,term):
    sum = 0
    for i in range(term+1):
        sum += (x**i )/ (factorial(i))
    return sum

print(e_power_x(3,2))