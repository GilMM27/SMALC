#include <iostream>
using namespace std;

int main() {
    int n; // declara n
    cout << "Ingresa un numero: "; // imprime
    cin >> n; // pide n
    for (int i = 1; i <= n; i+=2) {
        cout << i << endl;
    }
    return 0;
}