#include<iostream> 
using namespace std; 
int main() { 
long long int a,b,c,d;
cin>>a>>b>>c>>d; 
if (a<b&&a<c&&a<d) 
cout <<"Amr"; 
else if (b<a&&b<c&&b <d) 
cout <<"Waleed"; 
else if (c <a&&c <b&&c <d) 
cout<<"Mustafa"; 
else if ( d<a&&d <b&&c >d)
cout<<"Youssef"; 
else 
cout <<"We are the best"; 
return 0;
}	