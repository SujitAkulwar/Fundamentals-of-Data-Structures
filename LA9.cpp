#include <iostream>
using namespace std;

int size = 7;
int stack[7];
int top = -1;
bool isFull(){
    int size = 7;
	if(top>size){
	    return true;  
	}
	else{
	    return false;
	}
}

bool isEmpty(){
	if(top==-1){return true;}
	return false;

}

void push(int element){
	if(isFull()){
	cout<<"the stack is full , so push operation is not available !! "<<endl;
	return;
	}
	top++;
	stack[top]=element;
	cout<<element<<" is pushed into the stack "<<endl;
}

int pop(){
	if(isEmpty()){
		cout<<"stack is empty !!"<<endl;
		return -1;
	}
	return (stack[top]);
}

int main(){
	int ch=1;
	do{
		cout<<"enter \n\t 1 . push \n\t 2 . pop \n\t 3 . for size \n\t 4 . to exit "<<endl;
		cin>>ch;
		switch(ch){
			case 1 : int el;
				cout<<"enter the positive integer to push"<<endl;
				cin>>el;
				push(el);
				break;
			case 2 : el = pop();
				if(el!=-1){
					cout<<"the poped element is "<<el<<endl;
					top--;
				}
				break;	
			case 3 : cout<<"size of stack is " <<top+1<<endl;
			break;
			default : cout<<" end the program "<<endl;
			ch=0;
		}
	}while(ch!=0);
}








