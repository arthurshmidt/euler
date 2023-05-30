# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def even(n):
    return n/2

def odd(n):
    return 3*n+1

if __name__ == "__main__":
    # set initial conditions
    num = 1 
    chain_count = 0
    max_chain = { "number" : 0, "count": 0 }

    while num <= 1000000:
        num = num +1
        n = num
        chain_count = 1
        while n > 2:
            if n % 2 == 0:
                n = even(n)
                chain_count = chain_count + 1
            else:
                n = odd(n)
                chain_count = chain_count + 1
        if chain_count > max_chain["count"]:
            max_chain["count"] = chain_count
            max_chain["number"] = num
    print(f'Number: {max_chain["number"]}')
    print(f'Chain count: {max_chain["count"]}')



