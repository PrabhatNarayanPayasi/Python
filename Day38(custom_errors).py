# a = int(input("Enter any value between 5 and 9"))

# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")
 
 
 
 
'''
Raising Custom errors
In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass
try:
  # code ...
except CustomError:
  # code...
This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.
 '''
w=input('Enter words')
str = "QUITE";
str1 = "quite";
if(w!=str):
  if(w!=str1):
    raise("Error occured")