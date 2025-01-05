// #include <iostream>

// using namespace std;

// int main() 
// {
//   cout << "This computing environment uses:" << endl;
//   cout << sizeof(char) << " byte for chars" << endl;
//   cout << sizeof(short int) << " bytes for shorts" << endl;
//   cout << sizeof(int) << " bytes for ints" << endl;
//   cout << sizeof(long int) << " bytes for longs" << endl;
//   cout << sizeof(float) << " bytes for floats" << endl;
//   cout << sizeof(double) << " bytes for doubles" << endl;
//   cout << sizeof(bool) << " byte for bools" << endl;
//   cout << sizeof(int *) << " bytes for pointers" << endl;
// }
#include <iostream>

using namespace std;

void greet() 
{
    cout << "Ave user!" << endl;
}

void greet_many_times(int how_many_times) 
{
    while (how_many_times > 0) {
        greet();
        how_many_times--;
    }
}

int main() 
{
    int size_of_ego;

    cout << "How big is your ego? [km]" << endl;
    cin >> size_of_ego;
    greet_many_times(1 + size_of_ego);
}