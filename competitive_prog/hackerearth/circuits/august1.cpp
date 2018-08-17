#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

char *removeDuplicate(char a[], int n) {

   // Used as index in the modified string
   int index = 0;   
    
   // Traverse through all characters
   for (int i=0; i<n; i++) {
        
     // Check if a[i] is present before it  
     int j;  
     for (j=0; j<i; j++) 
        if (a[i] == a[j])
           break;
      
     // If not present, then add it to
     // result.
     if (j == i)
        a[index++] = a[i];
   }
    
   return a;
}

 
// Driver code
int main()
{
int t;
char a[1000],a1[1000];
int len=0,len1=0;
int i,j;
int count=0;
int b[1000];
int max=0;
int store;

   cin >> a;
   
   for (t=0;a[t]!='\0';t++) {
   a1[t]=a[t];
   len++;
   }

   for (t=0;a1[t]!='\0';t++)
   len1++;

   for (t=0;t<len1;t++) {
       for (int t1=0;t1<len;t1++) {
           if (a[t] == a[t1]) {
           count++;
           b[t] = count;
           }
       }
       count=0;
   }

    for (t=0;t<len1;t++) {
        if (b[t] > max) {
        max = b[t];
        store = t;
        }
    }
    
int count1=0;
    
   for(i=0; i<len; i++)
	{
		if(a[i]==a1[store])
		{
			for(int j=i; j<(len-1); j++)
			{
				a[j]=a[j+1];
			}
			count1++;
			break;
		}
	}
//    int n = sizeof(a) / sizeof(a[0]);
//    cout << removeDuplicate(a, n) << '\n';
cout << count1-1;
   return 0;

}
