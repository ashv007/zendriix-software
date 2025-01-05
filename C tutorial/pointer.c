// Program to demonstrate the usage of __GCC_ATOMIC_POINTER_LOCK_FREE
#include<stdio.h>
int main(){
    int main = 20;
    int *p;
    p = &rename;
    printf("address of variable name :%u",&rename);
    printf("address stored in pointer variable p : %u",p);
    printf("value of variable name:%d",*p);
    return 0;
}