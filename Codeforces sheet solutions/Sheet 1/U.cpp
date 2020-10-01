#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int x;
	 double y,r;
	cin>>x>>y;
	if(x==1)
	r=(4.00)*y;
	else if(x==2)
	r=(4.50)*y;
	else if(x==3)
	r=(5.00)*y;
	else if(x==4)
	r=(2.00)*y;
	else if(x==5)
	r=(1.50)*y;

	cout<<fixed<<setprecision(2)<<"Total: R "<<r<<endl;
	

	return 0;
}