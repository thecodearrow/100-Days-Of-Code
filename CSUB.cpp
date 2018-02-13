/*

CODECHEF

Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.
*/

#include <bits/stdc++.h>
using namespace std;
int main() {
	// your code goes here
	long long int T,l,count;
	string str;
	cin>>T;
	for(int i=0;i<T;i++){
	    count=0;
	    cin>>l;
	    cin>>str;
	    for(int m=0;m<l;m++){
	        if(str[m]=='1'){
	        count++;
	        }
	        }
	      
	
	cout<<(count*(count+1))/2<<"\n";
	}  
 
}