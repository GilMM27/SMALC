#include <iostream>

using namespace std;

int doble(int x){
    return 2 * x;
}

int main(){
    cout<<"ingresa un num: ";
    int num;
    cin>>num;
    cout<<"el doble de "<<num<<" es "<<doble(num);
    
    return 0;
}