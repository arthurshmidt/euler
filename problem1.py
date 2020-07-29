

if __name__ == "__main__":
    
    values = []
    max_value = int(input("Enter max number: "))
    for i in range(1,max_value):
        if ((i % 3 == 0) or (i % 5 == 0)):
            print(i)
            values.append(i)
    print("Number of Multiples: {}".format(len(values)))
    print("Sum of Multiples: {}".format(sum(values)))
