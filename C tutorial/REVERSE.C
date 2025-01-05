// Program to reverse a sentence entered by user using recursion
#include<stdio.h>
void reverse();
void main()
{
    printf("Please enter a sentence : \n");
    reverse();
}
void reverse()
{
    char word;
    scanf("%c", &word);
    if(word != '\n')
    {
        reverse();
        printf("%c",word);
    }
}
