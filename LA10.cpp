#include <iostream>
#include <string.h>

using namespace std;
const int Max = 50;
class infix{
	private :
		char target[Max], stack[Max];
		char *s, *t;
		int top;
	public :
		infix();
		void setExpr(char *str);  
		void Push(char c); 
		char Pop();        
		void convert();
		int Pri(char c);  
		void show();
} ;


infix :: infix( ){
	top = -1 ;
	strcpy ( target, "" ) ;
	strcpy ( stack, "" ) ;
	t = target ;   
	s = ""  ;
}


void infix :: setExpr ( char *str ){s = str ;}

void infix :: Push (char c){
	if (top==Max){cout << "\nStack is overflow\n" ;}
	else{
		top++ ;
		stack[top]= c;
	}
}

char infix :: Pop( ){
	if(top==-1){
		cout << "\nStack is Underflow\n" ;
		return -1 ;
	}
	else{
		char high = stack[top] ;
		top-- ;
		return high ;
	}
}
void infix :: convert( ){
	while ( *s ){
		if ( *s == ' ' || *s == '\t' ){
			s++ ;
			continue ;
		}
		if ( isdigit ( *s ) || isalpha ( *s ) ){
			while ( isdigit ( *s ) || isalpha ( *s ) ){
				*t = *s ;
				s++ ;
				t++ ;
			}
		}
		if ( *s == '(' ){
			Push(*s) ;
			s++ ;
		}
		char opr ;
		if ( *s == '*' || *s == '+' || *s == '/' ||*s == '-'){
			if ( top != -1 ){
				opr = Pop( ) ;
				while ( Pri( opr ) >= Pri ( *s ) )
{
					*t = opr ;
					t++ ;
					opr = Pop( ) ;
				}
				Push ( opr ) ;
				Push ( *s ) ;
			}
			else
				Push ( *s ) ;
			s++ ;
		}
		if ( *s == ')' )
		{
			opr = Pop( ) ;
			while ( ( opr ) != '(' )
			{
				*t = opr ;
				t++ ;
				opr =  Pop( ) ;
			}
			s++ ;
		}
	}
	while ( top != -1 )
	{
		char opr = Pop( ) ;
		*t = opr ;
		t++ ;
	}
	*t = '\0' ;
}
int infix :: Pri ( char c )
{
	if ( c == '^' )
		return 3 ;
	if ( c == '*' || c == '/')
		return 2 ;
	else
	{
		if ( c == '+' || c == '-' )
			return 1 ;
		else
			return 0 ;
	}
}

void infix :: show( )
{
	cout << target ;    
}

int main( )
{
	char expr[Max] ;
	infix q ;

	cout << "\nEnter an Infix Expression " ;
	cin.getline ( expr, Max ) ;

	q.setExpr ( expr ) ;
	q.convert( ) ;

	cout << "\nThe postfix expression is: " ;
	q.show() ;
}





