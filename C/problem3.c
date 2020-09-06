/* the largest prime factor
 *
 * The prime factors for 13195 are 5, 7 13, and 29.
 * 
 * What is the largest prime factor for the number 600851475143
 */

#define MAX_ARRAY 50

#include <stdio.h>

int largest_prime_factor(int number);

int main() {
	int number = 0;
	int factor = 0;
    
   	printf("Enter number to factor:> ");
    scanf("%d", &number);

    factor = largest_prime_factor(number);
	printf("The largest prime factor is: %d\n",factor);

    return 0;
}

int largest_prime_factor(int number){
	
	int p_factor = 2;
	int d_number = number;
    int count = 0;
    int p_factors[MAX_ARRAY] = {0};

	while(d_number / p_factor != 1) {
		if (d_number % p_factor == 0) { 
			d_number = d_number / p_factor;
            printf("1. d_number = %d, ",d_number);
            printf("1. p_factor = %d, ",p_factor);
            p_factors[count] = p_factor;
        }
		else if (d_number % p_factor > 0) {
			p_factor += 1;
            printf("2. d_number = %d, ",d_number);
            printf("2. p_factor = %d, ",p_factor);
        }
        if (d_number / p_factor == 1) {
            printf("3. d_number = %d, ",d_number);
            printf("3. p_factor = %d  ",p_factor);
            p_factors[count] = p_factor;
        }
        count += 1;
        printf("\n");
	}

    for(int i=0; i < MAX_ARRAY; i++)
        printf("Factor: %d\n",p_factors[i]);
	return p_factor;	
}
