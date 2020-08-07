# The largest prime factor 
#
# The prime factors for 13195 are 5, 7, 13, and 29.
# 
# What is the largest prime factor for the number 600851475143

def largest_prime_factor(number):
    p_factors = []
    d_number = number
    p_factor = 2
    while (d_number / p_factor != 1):
        if (d_number % p_factor == 0):
            d_number = d_number / p_factor
            p_factors.append(p_factor)
        elif (d_number % p_factor > 0):
            p_factor += 1
        if (d_number / p_factor == 1):
            p_factors.append(p_factor)

    return p_factors
        

if __name__ == "__main__":
    number = int(input("Enter number to factor:> "))
    p_factors = largest_prime_factor(number)
    print(p_factors)
