#include <stdio.h>

int fact(int n){
    if (n == 1){
        return n;
    } else {
        return n * fact(n-1);
    }
}

int main(void){
    int n = 5;
    int f = fact(n);
    printf ("Factorial is %d\n",f);
}