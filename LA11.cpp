#include<iostream>
using namespace std;
int size = 4;
int stack[4];
int top = -1;
bool isfull()
   {
       if(top>=(size-1))
       {
           return true;
       }
       return false;
   }

bool isempty()
{
    if(top==-1)
    {
        return true;
        
    }
    return false;
}

void push(int element)
{
    if(isfull())
    {
        cout<<"The stack is full, we cannot push element in stack !"<<endl;
        
    }
    else{
    top++;
    stack[top]=element;
    cout<<"the element pushed into the stack"<<endl;
    }
}

int pop()
{
    if (isempty())
    {
        cout<<"Your stack is empty we cannot pop the element"<<endl;
        return -1;
    
    }
    return stack[top];
}
    


int main()
{
    int ch=1;
    do{
        cout<<"\n\nEnter the choice :"<<endl
        <<"1.Push element in stack"<<endl
        <<"2.Pop the element in stack"<<endl
        <<"3.for size"<<endl
        <<"4.Exit"<<endl;
        
        cin>>ch;
        switch(ch)
        {
            case 1: int ele;
            
            cout<<"Enter the positive element to push"<<endl;
            cin>>ele;
            push(ele);
            break;
            
            
            case 2: ele= pop();
            if(ele != -1)
            {
            cout<<"The popped element is"<<ele;
            top--;
            }
            break;
            
            case 3: cout<<"Size of the stack is "<<top+1<<endl;
            break;
            
            default:
            cout<<"Program Ended !";
            ch=0;
        }    
        }while(ch!=0);
        
        
    
}




