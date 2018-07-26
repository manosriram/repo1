#include <iostream>

using namespace std;

int main() {
    int a[1000000],t,n,r;
    int temp;

    cin >> n >> r;

    if (r <= n && n<=100000) {

    for (t=0;t<n;t++)
    cin >> a[t];

    for (t=0;t<r;t++) {
        temp = a[0];

        for (int i=0;i<n-1;i++) {
            a[i] = a[i+1];
        }
        a[n-1] = temp;
    }

    for (t=0;t<n;t++)
    cout << a[t] << " ";



    }   
}