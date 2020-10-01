#include<iostream>
#include<iomanip>
using namespace std;
int main()
{cout<<fixed<<setprecision(9);
	double radius,area;
	cin>>radius;
	area = 3.14159*radius*radius;
	cout<<"Area = "<<area<<endl;
	return 0;
}