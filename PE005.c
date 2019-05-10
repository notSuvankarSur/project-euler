#include <stdio.h>

int min(int a, int b){
    return a<b?a:b;
}

int gcd(int a,int b){
    int x = min(a,b);
    if(a%x==0 && b%x==0){
        return x;
    }
    for(int i=x-1;i>0;i--){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
}

int lcm(int a, int b){
    int x=gcd(a,b);
    if(x==min(a,b)){
        return b;
    }
    else if(x==1){
        return a*b;
    }
    else
        return x * (a/x) * (b/x);
}

int main(){
    
    int i,z;
    int x = 11;
    int y = 12;
    
    while(y<20){
        z=lcm(x,y);
        x=z;
        y++;
        
    }
    printf("%d",lcm(7,z));
    
    return 0;
}