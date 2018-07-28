/*
Xenny and Yana were very keen to celebrate Valentine's Day at their home. To make preparations for the celebration, they listed down N tasks that they had to complete.

To complete the ith task, Xenny takes Xi seconds and Yana takes Yi seconds. In order to minimize the disparity in tasks performed, they decide to do the tasks alternatingly. If Xenny did the 1st task, then Yana would just wait and watch him until he completes the task. After that, Yana would start the 2nd task, and while she does her task, Xenny would just watch her. He would start the 3rd task only after her completion, and they would keep doing tasks alternatingly uptil the Nth task. They could also do tasks in the other order - that is, Yana could do the 1st task, after that Xenny could do the 2nd task, and so on. Their eventual goal was to minimize the total time taken by them to complete all N tasks.

Please help them find the minimum total time they would take to complete all N tasks.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each testcase contains a positive integer N - the number of tasks to be completed.

The second line contains N space-separated positive integers representing the time taken in seconds by Xenny to complete the ith task.

The third line contains N space-separated positive integers representing the time taken in seconds by Yana to complete the ith task.

Output

For each testcase, print a single line containing the minimum total time in seconds Xenny and Yana would take to complete the tasks.


*/

#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{   int testcase_no;
	int n;
 	vector<int> x;
 	vector<int> y;
 	cin>>testcase_no; 
 	if(testcase_no==0){
    cout<<0;
    }
 	else{
    for(int i=0;i<testcase_no;i++){
    cin>>n;
    for(int j=0;j<n;j++){
    int temp1=0;
    cin>>temp1;
    x.push_back(temp1);
    
    }
    for(int k=0;k<n;k++){
    int temp2=0;
    cin>>temp2;
    y.push_back(temp2);
    
    }
    int sum1=0,sum2=0;
    for(int i=0;i<n;i=i+2){
    sum1=sum1+x[i];
    sum2=sum2+y[i];
    }
    for(int i=1;i<n;i=i+2){
    sum1=sum1+y[i];
    sum2=sum2+x[i];
    }
    
    cout<<min(sum1,sum2);
    
    }
    
    
    
    
    
    }
 	
	return 0;
}