# Summation of primes

# The Sum of the primes below 10 is 2 + 3+ 5 +7 = 17.
#
# Find the sum of all the primes below two million.

if __name__ == "__main__":
    prime = False
    prime_numbers = [2]
    counter = 3
    while (counter < 2000000):
        for i in range(2,counter):
            if counter % i == 0:
               # print(f"Not Prime - counter: {counter}, range: {i}")
               prime = False
               break
            else:
                # print(f"Prime - counter: {counter}, range: {i}")
                prime = True
        if prime == True:
            prime_numbers.append(counter)
            print(f"Prime: {counter}")
        counter += 1
        prime = False
    print("Calculating the sum of the primes")
    prime_sum = sum(prime_numbers)
    print(f"Counter: {counter}")
    print(f"Sum of the primes: {prime_sum}")

