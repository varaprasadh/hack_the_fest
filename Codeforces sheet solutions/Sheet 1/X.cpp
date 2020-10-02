#include<iostream>
using namespace std;
int main()
{
	string month[] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
	int number;
	cin>>number;
	cout<<month[number-1];
	return 0;
}