/* the largest prime factor
 *
 * The prime factors for 13195 are 5, 7 13, and 29.
 * 
 * What is the largest prime factor for the number 600851475143
 */

#include <stdio.h>

int largest_prime_factor(int number);

int main() {
	int number = 0;
	int factor =0;
    
   	printf("Enter number to factor:> ");
    	scanf("%d\n", number);

       	factor = largest_prime_factor(number);
	printf("The largest prime factor is: %d\n",factor);

    	return 0;
}

int largest_prime_factor(int number){
	
	int p_factor = 2;
	int d_number = number;

	while(d_number / p_factor != 1) {
		if (d_number % p_factor == 0) 
			d_number = d_number / p_factor;
		else if (d_number / p_factor > 0)
			p_factor += 1;
	}
	return p_factor;	
}
