# If we list all the natrual numbers below 10 that are multiples of 
# 3 or 5, we get 3, 5, 6, and 9.  The sum of these multiples is 23.
#
# Find the sum of all the multiples from 3 or 5 below 1000.

if __name__ == "__main__":
    
    values = []
    max_value = int(input("Enter max number: "))
    for i in range(1,max_value):
        if ((i % 3 == 0) or (i % 5 == 0)):
            print(i)
            values.append(i)
    print("Number of Multiples: {}".format(len(values)))
    print("Sum of Multiples: {}".format(sum(values)))
