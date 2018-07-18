#include <iostream>
#include <algorithm>

using namespace std;
int counted=0;
int a[100],t,n,check,a1[100],m,n1,temp;
int track,out=0,out1=0;
static int rank1[100];
int record[100];


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

int addAlice(int a[100],int a1[100],int track,int n,int out,int out1) {

for (t=0;t<n+1;t++) {
    if (a[t]==track) {
        record[out1] = rank1[t];
        out++;
        out1++;         
    }
    else
    continue;
}
return record[out1];
}



int removeAlice(int a[100],int track,int n) {
    for(int i=0; i<n+1; i++)
	{
		if(a[i]==track)
		{
			for(int j=i; j<(n-2); j++)
			{
				a[j+1]=a[j+2];
			}
			counted++;
			break;
		}
	}
    return a[n+1];
}



int sortIt(int a[100]) {
    sort(a, a+n+1, greater<int>());
    return a[n+1];
}

int main() {
    
    cin>>n;
    
    for (t=0;t<n;t++)
    cin>>a[t];


    cin >> n1;
    cout << "Enter Alice's Scores : " << endl;
//Alice Scores...
    for (t=0;t<n1;t++)
    cin >> a1[t];
   

    rankCounter(a);

    for (t=0;t<n;t++)
    cout<<"Rank of Value " << " " << a[t] << " is " << rank1[t] << endl;
    
    for (t=0;t<n1;t++) {
        a[n+2+t] = a1[t];
        sortIt(a);
        rankCounter(a);
        addAlice(a,a1,track,n,out,out1);
        removeAlice(a,track,n);
    }
for (t=0;t<n;t++)
cout << record[t];
    }

