// Program to find Maximum element in an array
#include<stdio.h>
int main(){
    int array[10],maximum,size,i,location =1;
    printf("enter the number of elements in an array:");
    scanf("%d",&size);
    printf("enter %d element \n",size);
    for(i = 0;i<size;i++)
        scanf("%d",&array[i]);
    maximum = array[0];
    for(i=1;i<size;i++)
    {
        if (array[i]>maximum){
            maximum = array[i];
            location =i+1;

        }   
    }
    printf("Maximum element is present at loaction %d and it value is %d",location,maximum);
    return 0;
}