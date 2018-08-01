#include <iostream>

using namespace std;

int main() {
    int n,k,a[100000],t;
    int i,j;
    int cnt=0;
    cin >> n >> k;

    i = 0;
    j = n-1;

    for (t=0;t<n;t++)
    cin >> a[t];

while (i<j) {
    if (a[i]-a[j] == k || a[j]-a[i] == k ) 
        cnt++;
        
    
    if (a[i] - a[j] > k) 
    i++;
    
    else
    j--;
}

    cout << cnt;
    cout << endl;

}