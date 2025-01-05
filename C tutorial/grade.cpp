// #include <iostream>

// using namespace std;

// int main()
// {
// 	double a = 0.1;
// 	double b = 0.4;
// 	double c = 0.3;

// 	if(a + b != c)
// 		cout << "Your computer is out of order";
// }
/* finding the larger of two numbers */

#include <iostream>

using namespace std;

int main() 
{
  /* the two numbers */
  int number1, number2;

  /* read two numbers */
  cin >> number1;
  cin >> number2;

  /* we will save the larger number here */
  /* we temporarily assume that the former number is the larger one */
  /* we will check it soon */
  int max = number1;

  /* we check if the assumption was false */
  if (number2 > max)
      max = number2;

  /* we print the result */
  cout << "The larger number is " << max << endl;
}