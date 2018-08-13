#include <iostream>

using namespace std;

int main() {
    string s[10];
    int n,t;
   
    cin >> n;

    for (t=0;t<n;t++)
    cin >> s[t];

    if (s[0] == s[1])
    cout << "Yes";

    else
    cout << "No";
}