#include <stdio.h>
#include <stdlib.h>

int main(){
    double n;
    double a;
    char p;
    int limit=0;
    printf("NO:\n");
    scanf("%lf",&n);
    printf("NO:\n");
    scanf("%lf",&a);
    printf("Enter the operation symbol:\n");
    scanf(" %c",&p);
    while(limit == 0){
        if(p=='+'){
            printf("%f",a+n);
    }   else if(p=='-'){
            printf("%f",a-n);

    }   else if(p=='*'){
            printf("%f",a*n);

    }   else{
        printf("Wrong O");
    }
    return 0;
 }
}

