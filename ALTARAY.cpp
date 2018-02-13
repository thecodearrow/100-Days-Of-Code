/*
CODECHEF

There's an array A consisting of N non-zero integers A1..N. A subarray of A is called alternating if any two adjacent elements in it have different signs (i.e. one of them should be negative and the other should be positive).

For each x from 1 to N, compute the length of the longest alternating subarray that starts at x - that is, a subarray Ax..y for the maximum possible y ≥ x. The length of such a subarray is y-x+1.

*/

#include <bits/stdc++.h>
 
using namespace std;
 
#define LL long long
int main()
{ LL int T,n,temp;
    array<int,1000000> a;
    array<LL int,100000> len;
    cin>>T;
    while(T--){
       cin>>n;
       for(LL int i=0;i<n;i++){
           cin>>temp;
           if(temp>=0){
               a[i]=1;
              
           }
           else{
              a[i]=-1;
           }
       }
       
       len[n-1]=1;
       for(LL int i=n-2;i>=0;i--){
           if(a[i]*a[i+1]<0){
              len[i]=len[i+1]+1; 
           }
           else{
               len[i]=1;
           }
           
       }
       
       for(int i=0;i<n;i++){
           cout<<len[i]<<" ";
           
           
       }
       
       
       cout<<"\n";
       
        
        
    }
    
 
    return 0;
}
 