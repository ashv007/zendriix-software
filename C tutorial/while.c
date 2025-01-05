// program to convert celsius tempreture into fahenheit and kelvin
#include<stdio.h>
int main(){
   float celsius,fahr,kelvin;
   float lower,upper,step;
   lower = 0;
   upper =100;
   step =10;
   celsius =lower;
   while (celsius<=upper)
   {
       fahr =(celsius * 1.8)+32;
       kelvin=celsius+273.15;
       printf("%d \t %d\t %d\n",celsius,fahr,kelvin);
       celsius =celsius + step;
       /* code */
   }
   
    
    
}