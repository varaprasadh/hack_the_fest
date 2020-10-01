#include<iostream>
#include<ctype.h>
using namespace std;
int main()
{
	char character;
	cin>>character;
	if(character == tolower(character))
	{
		cout<<(char)toupper(character)<<endl;
	}
	else
	{
		cout<<(char)tolower(character)<<endl;
	}
	return 0;
}