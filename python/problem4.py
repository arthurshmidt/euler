# Largest Palindrome product
#
# A palindromic number reads the same both ways.  The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91x99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

if __name__ == "__main__":
    
    max_val = 0
    for i in range(100,1000,1):
        for v in range(100,1000,1):
            value = i * v
            f_value = str(value)
            r_value = f_value[::-1]
            if (f_value == r_value) and (value > max_val):
               max_val = value

    print(max_val)
