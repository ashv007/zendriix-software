#include<stdio.h>
void swap(int a,int b);
void main(){
    int x,y;
    printf("enter the value of x and y:\n");
    scanf("%d \n %d",&x,&y);
    printf("values before swap \n x=%d \n y=%d,x , y");
    swap(x , y);
}
void swap(int a,int b){
    int temp;
    temp =a;
    a=b;
    b=temp;
    printf("\n value after\n x=%d \n y=%d, a , b ");
}