#include <stdio.h>

int max(int x, int y){
    return x>y?x:y;
}

int isPallindrome(int n){
    int rev = 0;
    int i = n;
    int rem = 1;
    while(i>0){
        rem = i%10;
        i = i/10;
        rev = rev*10 + rem;
    }
    if(rev==n){
        return 1;
    }
    else
        return 0;
}


int main()
{
    int x,y;
    x = y = 999;
    int pal=1;

    for(int i=x;i>99;i--){
        for(int j=y;j>99;j--){
            if(i*j>pal && isPallindrome(i*j)){
        
                pal=i*j;
            
            }
        }
        
    }
    printf("%d",pal);
    
    return 0;
}