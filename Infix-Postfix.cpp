#include <iostream>
#include<string.h>
#include<ctype.h>

//infix to postfix
using namespace std;

int top=-1;
char a[100];
void push(char op)
{a[++top]=op;

}

char pop()
{
    char trash=a[top--];
    return(trash);
}

int priority(int x)
{ if(x=='(')
     return 0;
    else if(x=='+' || x=='-')
     return 1;
     else if(x=='*' || x=='/')
     return 2;
     else if(x=='^')
     return 3;

}
int main()
{
    int t,num;
    string input;
    cin>>t;
    char x;
       if(t<101){
          for(num=1;num<=t;num++)
            {
                cin>>input;
                for(int i=0;i<input.length();i++)
                    {
                        if(isalpha(input[i]))
                            cout<<input[i];
                        else if(input[i]=='(')
                                push(input[i]);
                        else if(input[i]==')')
                        {
                            while(a[top]!='(')
                            {   x=pop();
                                cout<<x;
                            }
                            top--;

                        }
                        else{
                                while(priority(input[i])<=priority(a[top]) && top!=-1)
                                {
                                    x=pop();
                                    cout<<x;
                                }
                                push(input[i]);

                            }


                        }

                        while(top!=-1) //Final pop
                        {
                            x=pop();
                            if(x!='(')
                            cout<<x;

                        }
                        cout<<"\n";


               }
       }

            }
