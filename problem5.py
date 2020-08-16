# Smallest Multiple
#
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?
from os import system


if __name__ == "__main__":
    flag = True
    counter = 20
    while(True):
        for i in range(1,21):
            if counter % i != 0:
                flag = False
                # print("False")
            # else:
                # print("True")
        print(f"Flag: {flag} Counter: {counter}")
        if flag:
            break
        flag = True
        # print(counter)
        counter += 20
