/*
To check if given points are vertices of a square
*/

#include<bits/stdc++.h>
using namespace std;

float dist(pair<int,int> &p1,pair<int,int> &p2){
 
return sqrt((pow(p1.first-p2.first,2)+pow(p1.second-p2.second,2)));   
    
    
}
int main(){

    array<pair<int,int>,4> c;
    float d[4];
    
    for(int i=0;i<4;i++){
        cin>>c[i].first>>c[i].second;
        
    }
    
    
    
    for(int i=1;i<4;i++){
        d[i-1]=dist(c[0],c[i]);
    }
    
    float l;
    //find l
    if(d[0]==d[1]){
        l=d[0]; 
    }
    else{
        l=d[2];
    }
    int lcount=0,root2lcount=0;
    for(int i=0;i<3;i++){
        if(l==d[i]){
            lcount++;
        }
         else if ((int)(sqrt(2)*l)==(int)d[i]){
           
            root2lcount++;
        }
    }
    if(lcount==2 && root2lcount==1){
        cout<<"square";
    }
    else{
        cout<<"not square";
    }
    
    
	return 0;
}
