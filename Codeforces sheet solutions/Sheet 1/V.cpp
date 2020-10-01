#include <iostream>
using namespace std;
int main()
{
int x,y;
int z;
char s,o;
cin>>x>>s>>y>>o>>z;
if ((s=='+' && x+y==z)||(s=='-' && x-y==z)||(s=='*' && x*y==z))
	cout<<"Yes";
else if(s=='+' && x+y!=z)
	cout<<x+y;
else if(s=='-' && x-y!=z)
	cout<<x-y;
else if (s=='*' && x*y!=z)
	cout<<x*y;
return 0;
}