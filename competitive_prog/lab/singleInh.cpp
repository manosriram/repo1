#include <iostream>
using namespace std;

class first {
    public:
    int a,b;

    void getV() {
        cin >> a >> b;
    }

    void showV() {
        cout << a << " " <<  b << " ";
    }

};

class second:public first {
    public:
    void changeV() {
        a = 10;
        b = 20;
    }

    void showV() {
        cout << a << " " <<  b << " ";
    }
};

class third:private first {
    public:
    void changeV1() {
        a=40;
        b=90;
    }

    void showV() {
        cout << a << " " <<  b << " ";
    }
};

int main() {
    first ob1;
    second ob2;
    third ob3;
    

    ob1.getV();
    ob1.showV();

    ob2.changeV();
    ob2.showV();
    
    ob3.changeV1();
    ob3.showV();


}