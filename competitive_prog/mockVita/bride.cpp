#include <iostream>

using namespace std;

int main() {
    int a[100][100],b[100][100],i,j,t,n,r,c,cnt=0;
    int max;
    
     cin >> r >> c;

     for (i=1;i<r+1;i++) {
         for (j=1;j<c+1;j++) {
             cin >> a[i][j];
         }
     }

     for (i=1;i<r+1;i++) {
         for (j=2;j<c+1;j++) {
             if (a[i][j] == 1) {
                 if (a[i][j-1]==1)
                 cnt++;

                 if (a[i][j+1]==1)
                 cnt++;

                 if (a[i-1][j]==1)
                 cnt++;

                 if (a[i+1][j]==1)
                 cnt++;

                 if (a[i+1][j-1]==1)
                 cnt++;

                 if (a[i-1][j+1]==1)
                 cnt++;

                 if (a[i-1][j-1]==1)
                 cnt++;

                 if (a[i+1][j+1]==1)
                 cnt++;

                 b[i][j]=cnt;
                 cnt = 0;

             }

             if (a[i][j]!=1) {
             b[i][j]=0;

             
             }
         }
     }

     b[1][1] = 1;
     
     max = 0;

     for (i=1;i<r+1;i++) {
         for (j=2;j<c+1;j++) {
             if (b[i][j] > max)
             max = b[i][j];

             else
             continue;
         }
     }
     
if (max>=1) {
     for (i=1;i<r+1;i++) {
         for (j=1;j<c+1;j++) {
             if (b[i][j]==max && max >= 1 ) {
                 cout << i << ":" << j << ":" << max;
                 break;
             }
             }
             
         }
     }

else if (max==0)
cout << "No suitable girl found" << endl;

    //  for (i=1;i<r+1;i++) {
    //      for (j=1;j<c+1;j++) {
    //          cout << b[i][j];
    //      }
    //      cout << endl;
    //  }

}