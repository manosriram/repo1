#include <iostream>

using namespace std;

int main() {
    int n,a[100],i,j,t,b[100];
    int x,cnt=0,tst,count=0;
    
    cin >> tst;

    while(count<tst) {

    cin >> n >> x;

    for (t=0;t<n;t++)
    cin >> a[t];
    
    for (i=0;i<n;i++) {
        for (j=i+1;i<n-i;i++) {
            if (a[i]+a[j]+a[j+1]+a[j+2] == x)
            cnt++;

            else
            continue;
        }
    }

    if (cnt>0)
    b[count] = 1;
    
    count++;
    cnt=0;
    }

    for (t=0;t<count;t++)
    cout << b[t];
}