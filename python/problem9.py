# A Pythagorean triplet is a set of natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet fro which a + b + c = 1000.
# Find the product abc.
import math

if __name__ == "__main__":
   for a in range(0,1000):
       for b in range(0,1000):
           c = math.sqrt(a**2+b**2) 
           num_sum = a+b+c
           num_product = a*b*c
           # print(f"A: {a}, B: {b}, C: {c}")
           # print(f"Sum = {sum}")
           if a < b and b < c and num_sum == 1000:
               print(f"A: {a}, B: {b}, C: {c}")
               print(f"Sum = {num_sum}")
               print(f"Product = {num_product}")
