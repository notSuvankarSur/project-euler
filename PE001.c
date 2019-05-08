#include <stdio.h>

int main(){
	int sum = 0;
	for(int index = 1; index < 1000; index++){
		if(index % 3 == 0 || index % 5 == 0){
			sum += index;
		}
	}
	printf("%d", sum);
}