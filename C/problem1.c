// If we list all the natural numbers below 10 that are multiples of
// 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples from 3 or 5 below 1000.
//
// Problems: 
// 1. Since the array is not dynamically increased if it is not big
// enough your answer will not be correct.  The max_value entered
// may exceed the max array length.
// 2. initialize, initialize, initialize!  I did not initialize my
// variables in my for-loops and they did not count correctly.
#include <stdio.h>

int main() {
	int max_value = 0, counter = 0, sum = 0;
	int values[10000] = {0};

	printf("Enter max number: ");
	scanf("%d",&max_value);

	for (int i = 0; i < max_value; i++) {
		if (((i % 3) == 0) || ((i % 5) == 0)) {
		       printf("%d\n",i);
		       values[counter] = i;
		       counter++;
		}
	}

	for (int j = 0; j < 10000; j++) {
		printf("%d\n",values[j]);
		sum += values[j];
	}

	printf("The sum of the values is: %d\n",sum);

	return 0;
}
