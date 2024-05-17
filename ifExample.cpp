#include <iostream>
using namespace std;

int main() {
    int edad;
    cout << "Ingresa tu edad: ";
    cin >> edad;
    if (edad >= 18) {
        cout << "Eres mayor de edad";
    } else if (edad >= 13) {
        cout << "Eres adolescente";
    } else {
        cout << "Eres un nino";
    }
    return 0;
}