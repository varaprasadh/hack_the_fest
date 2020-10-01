#include<iostream>
using namespace std;
int main()
{
	unsigned int n; cin>>n;
	(n/1000 %2 == 0)?cout<<"EVEN"<<endl:cout<<"ODD"<<endl;
	return 0;
}