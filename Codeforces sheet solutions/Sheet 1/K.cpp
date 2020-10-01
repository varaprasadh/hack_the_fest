#include<iostream>
using namespace std;
int main()
{
int n,m;
char s;
cin>>n>>s>>m;
if((n>m&&s=='>')||(n<m&&s=='<')||(n==m&&s=='='))
cout<<"Right";
else
cout<<"Wrong";
return 0;
}
