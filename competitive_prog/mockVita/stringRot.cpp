#include <iostream>

using namespace std;

int t,n,len=0;

char lock[30];
static int cnt;
string s;
char temp;

char leftRotate(char a[100],int a1[100]) {

  for (t=0;t<a[t];t++) {
      temp = s[0];

      for (int i=0;i<n-1;i++) {
          s[i] = s[i+1];
      }
      s[n-1] = temp;
  }
  return s[0];
}

char rightRotate(char a[100],int a1[100]) {
  for (t=0;t<a[t];t++) {
      temp = s[len-1];

      for (int i=len-1;i>=0;i--) {
          s[i+1] = s[i];
      }
      s[0] = temp;
}
return s[0];
}


int main() {
  char a[100];
  int a1[100];
  cin >> s;

   for (t=0;s[t]!='\0';t++)
   len++;
cin >> n;
  for (t=0;t<n;t++) {
    cin >> a[t] >> a1[t];
  }

  for (t=0;t<n;t++) {
    if (a[t]=='L') {
      lock[cnt] = leftRotate(a,a1);
      cnt++;
    }
    if (a[t]=='R') {
      lock[cnt] = rightRotate(a,a1);
      cnt++;
    }
  }

  for (t=0;t<cnt;t++)
  cout << lock[t];


}
