#include <stdio.h>
void main(){
    int day;
    printf("enter any days:\n");
    scanf("%d",&day);
    switch (day){
    case /* constant-expression */1:printf("sunday");        /* code */
    break;
    case2:printf("maonday");    
    break;
    case3:printf("tuesday");
    break;
    case4:printf("thurseday");
    break;
    case5:printf("wedneday");
    break;
    case6:printf("friday");
    break;
    case7:printf("satureday");
    break;
    
    default:printf("enter valid input");
    break;
    }

}