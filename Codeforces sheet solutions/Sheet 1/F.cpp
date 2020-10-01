#include<iostream>
using namespace std;
void doNothing() {}
int main()
{
	unsigned int a,b; cin>>a>>b;
	(a<b)?swap(a,b):doNothing();
	(a % b == 0)?cout<<"Multiples"<<endl:cout<<"No Multiples"<<endl;
	return 0;
}
