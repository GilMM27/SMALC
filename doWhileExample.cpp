#include <iostream>
using namespace std;

int main() {
    int num; // declarar num
    do {
        cout<<"ingresa un numero: ";
        cin>>num;
    } while (num >= 0 && num <= 10);
    cout<<"Se ingreso un numero que no esta entre 0 y 10";
    return 0;
}