#include <iostream>

using namespace std;

int a[100],t,n,check,a1[100],m;

static int rank1[100];
int rankCounter(int a[100]) {

int count;
    count = 2;
    rank1[0] = 1;
    // LeaderBoard Ready.
    for (t=0;t<n;t++) {
        if (a[t] == a[t-1]) {
            rank1[t] = rank1[t-1];
        } 
        if (a[t] != a[t-1] && t!=0) {
                rank1[t] = count++;
        }
        }
    return rank1[t];
}


int main() {
    
    cin>>n;
    
    for (t=0;t<n;t++)
    cin>>a[t];

    rankCounter(a);

    a[n+1] = 1000;
    rankCounter(a);
    
    cout<<"Rank of Value " << " " << a[n+1] << " is " << rank1[n] << endl;
    for (t=0;t<n;t++)
    cout<<"Rank of Value " << " " << a[t] << " is " << rank1[t] << endl;

    
}