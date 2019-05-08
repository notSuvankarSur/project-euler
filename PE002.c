#include <stdio.h>


int main(){

	int a = 1;
	int b = 1;
	int sum = 0;
	int c = a + b;

// a, b, and c are temporary variables,
// as we need only the previous two terms to calculate the current term
// it can be seen that every third term is even, so we only add every third term

	while(1){

		sum += c;
		a = b + c;
		b = c + a;
		c = a + b;
		if (c > 4000000){
			break;
		}
	}

	printf("%d", sum );
	return 0;
}
