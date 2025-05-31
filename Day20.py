'''Python Functions
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:
=========================================================================
Built-in functions
Built-in functions
==========================================================================
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements
Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
Any parameters and arguments should be placed within the parentheses.
Rules to naming function are similar to that of naming variables.
Any statements and other code within the function should be indented.
Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:

def name(fname, lname):
    print("Hello,", fname, lname)
name("Sam", "Wilson")
Output:

Hello, Sam Wilson'''

'''def calc(a , b):
    print(a+b);
calc(20 , 4);
calc(2 , 4);
calc(22 , 4);
calc(2 , 44);
calc(2 , 45);
calc(2 , 40);
calc(20 , 40);  '''





'''
def isGreater(a , b):
    if(a>b):
        print("a is grater than b . ");
    else:
        print("a is less than b . ");
isGreater(2,4);
isGreater(3 , 2);'''

def add(a,b):
    print(a+b);
add(3,4)
add(-2 , 0)

def subs(a,b):
    print(a-b);
subs(3,2);
subs(4.9,3);
def name(fname , lname):
    print("Hello" , fname , lname);
name("Prabhat","Narayan");



# def funcname(param):
#     print("STATEMENT");
# funcname(param)