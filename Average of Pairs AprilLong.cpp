#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        map<long long,long long> m;
        map<long long,long long>::iterator it1,it2;
        long long n,i,count=0,temp;
        cin>>n;
        for(i=0;i<n;i++){
            cin>>temp;
            m[temp]+=1;
        }
        for(it1=m.begin();it1!=m.end();it1++){
            long long int f=it1->second;
            if(f>1){
                
                count=count+f*(f-1)/2;
            }
            for(it2=it1;it2!=m.end();it2++){
                long long int s=it1->first+it2->first;
                if(it1!=it2 && s%2==0 ){
                    
                    long long avg=s/2;
                    if(m[avg]>0){
                        
                        count=count+it1->second*it2->second;
                    }
                }
                
            }
            
        }
        cout<<count<<"\n";
    }
    
    return 0;
}