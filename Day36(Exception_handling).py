# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# # except IndexError:
# print("Index Error")
try:
    
    x = input("Enter the number :")
    for i in range(11):
        print(x*i);
except  Exception as e:
    print(f"Error occured {e}");
    
print("okk")




'''
Exception Handling
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. 
The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception
Example:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
Output:
Enter an integer: 6.022
Number entered is not an integer.
'''
2
2
