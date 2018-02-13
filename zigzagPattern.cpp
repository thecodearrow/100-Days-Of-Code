#include <bits/stdc++.h>
using namespace std;
/*

Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G   
  B   D   F   H
Now concatenate the two rows and ignore spaces 
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces 
in every row. We get "GSGSEKFREKEOE"





*/
int main() {
	// your code goes here
	string str = "GEEKSFORGEEKS";
	array<string,100> s;
	int direction; //1 for down -1 for up
	int n=3;
	int rows=0,index=0;
	char matrix[n][str.length()];
	for(int o=0;o<n;o++)
	for(int k=0;k<str.length();k++)
	matrix[o][k]='*';
	for(int i=0;i<str.length();i++){
	    s[rows]=s[rows]+str[i];
	    matrix[rows][index++]=str[i];
	    if(rows==n-1){
	        direction=-1;
	    }
	    if(rows==0){
	        direction=1;
	    }
	    if(direction==1){
	        rows++;
	    }
	    else{
	        rows--;
	    }
	    
	}
	for(int i=0;i<str.size();i++){
	    cout<<s[i];
	}
	cout<<"\n\n";
	for(int o=0;o<n;o++){
	for(int k=0;k<str.length();k++){
	    cout<<matrix[o][k];
	}
    cout<<"\n";
}
	return 0;
}
