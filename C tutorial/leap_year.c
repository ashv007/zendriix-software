// #include<stdio.h>
// int main(){
//     int year;
//     printf("enter the year:");
//     scanf("%d",&year);
    
//     (year%400==0)?printf("leap year"):printf("this is not leap year");

// }
#include<stdio.h>  
int min (int x,int y)
{
    return(x<y)?x:y;
}
int main()
{
    int a=20,b=60;
    int minimum = min (a,b);
    printf("minimum value %d",minimum);
    return 0;
}