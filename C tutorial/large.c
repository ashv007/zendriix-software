#include<stdio.h>
void main (){
    int x,y,z;
    printf("\n Enter the number : ");
    scanf("%d%d%d",&x,&y,&z);
    if(x>y && x>z)
    printf("the large number : x");
    else if(y>x && y>z)
    printf("the largest number:y");
    else
    printf("the largest number :z");
    
} 