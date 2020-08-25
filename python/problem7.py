# 10001st prime
#
# by listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see 
# that the 6th prime is 13.
#
# What is the 10001st prime number?

if __name__ == "__main__":
    prime = False
    num_primes = [2]
    counter = 3
    while (len(num_primes) < 10001):
        for i in range(2,counter):
            if counter % i == 0:
               # print(f"Not Prime - counter: {counter}, range: {i}")
               prime = False
               break
            else:
                # print(f"Prime - counter: {counter}, range: {i}")
                prime = True
        if prime == True:
            num_primes.append(counter)
            print(f"Prime: {counter}, Num Primes: {len(num_primes)}")
        counter += 1
        prime = False

