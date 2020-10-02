#include<iostream>
using namespace std;
int main()
{
	int a,b,c;
	a=0;
	b = a++; //a=1 here
	c = ++a; //a=2 here
	cout<<a<<endl;
	cout<<b<<endl;
	cout<<c<<endl;
	return 0;
}