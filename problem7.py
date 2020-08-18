# 10001st prime
#
# by listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see 
# that the 6th prime is 13.
#
# What is the 10001st prime number?

if __name__ == "__main__":
    
    num_primes = 2
    counter = 3
    while (True):
        for i in range(1,counter):
            if counter % i == 0 :
               print(f"counter: {counter}, range: {i}")
        counter += 1
