#include<iostream>
using namespace std;
int main()
{
	int n;

	while(cin>>n)
	{
		int w=0;
		if(n!=0)
		{
			for(int s=0; s<n; s++)
			{
				int a;
				cin>>a;
				if(a%2==0)
				{
					w=w+a;
					if(a==0)
					{
						break;
					}
				}
			}
			cout<<w<<endl;
		}
		else
		{
			break;
		}
	} 
	return 0;
}
