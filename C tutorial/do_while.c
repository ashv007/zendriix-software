// Program to add numbers untill user enters zero value
#include<stdio.h>
int main(){
    double num,sum=0;
    do
    {
        printf("enter a number :\n");
        scanf("%lf",&num);
        sum = sum+num;
        /* code */
    } while (num!=0.0);
    printf("Sun of positive numbers = %2.3lf",sum);
    return 0;
    
}