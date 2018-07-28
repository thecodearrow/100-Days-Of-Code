#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{	int a,n,k;
  	cin>>a>>n>>k;
 	
  	if(a<0 || a>1000000000 || n<0 || n>100 || k<1 || k>100){
    return 0;
    }
  	
 
 	//a=q*(n+1)+ (a%(n+1)) q packets containing n+1 packets each plus leftovers in a 
 	//b=a/(n+1) ....... here a is chamber 0, b is chamber 1 and so on! 
 
 	while(k--){
    cout<<a%(n+1)<<" ";
   	a=a/(n+1);
    }
	return 0;
      
      
}