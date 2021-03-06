# Highly divisible triagular number
#
# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Lets us list the factors of the first seven triangle number:
# 
#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
#
# We can see that 29 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?
import numpy as np


# input: number to be factored
# output: N/A
# return: array of factors
def factor(factor_number):
    factors = 0
#    factors = np.array([])
#    factors = []
    for i in range(1,factor_number+1):
        if factor_number % i == 0:
            factors += 1
#            factors = np.append(factors,[i])
#            factors.append(i)

    return factors

# input: number to triangle
# output: N/A
# return: triangular number
def triangular(triangular_number):
    triangular_value = 0
    for x in range(1,triangular_number+1):
        triangular_value += x

    return triangular_value

#
#   Main Program Execution
#
if __name__ == "__main__":
    count = 0
    t_number = 0
    num_factors = 0
#    for x in range(1,100):
#        print("{}, value {}".format(x,triangular(x)))
#        print("Factors: {}".format(factor(triangular(x))))

    while num_factors < 500:
        count += 1
        t_number = triangular(count)
#        factors = factor(t_number)
#        print(factors.size)
        num_factors = factor(t_number)
#        print(t_number)
        print(num_factors)
    print(t_number)

