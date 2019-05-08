#include <stdio.h>
int main()
{
    int largestPrimeFactor = 1;
    long int num = 600851475143;
    int i=2;
    /*
	It basically iterates over all the numbers starting from 2
	and finds the factors and divides the number, we'll only get
	prime facrors, as we're resetting i back to 2
    */
    while(i<=num){
        if(num%i==0){
            num = num/i;
            largestPrimeFactor = i;
            i=2;
        }
        else{
            i++;
        }
    }
    printf("%d",largestPrimeFactor);

    return 0;
}
}