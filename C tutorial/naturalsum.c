// Program to find the sum of natural numbers entered by user
#include <stdio.h>
int main(){
    int num,i,sum=0;
    printf("enter the value of num :");
    scanf("%d",&num);
    for(i=1;i<=num;i++){
        sum = sum + 1;}
    printf("sum of natural number is %d",sum);
    return 0;
    
}