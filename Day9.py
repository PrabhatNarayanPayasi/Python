            



# ----------------------------------------TYPECASTING----------------------------------------------------------

# kisi string ko int m badalna hi typecasting hota hai we can convet different types . 
# a = "2";
# b = "9";
# # print(a+b)
# # The conversion of one datatype to other datatype is known as typecasting.
# print(int(a) + int(b))

# # Impplicit Typecasting
# c = 1.9
# d=9
# print(c+d)


# Typecasting in python
# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# Two Types of Typecasting:


'''Explicit Conversion (Explicit type casting in python)
Implicit Conversion (Implicit type casting in python).


Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, 
is known as explicit type conversion.
# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
#Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
Output:
The Sum of both the numbers is 22
'''


'''Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python.
Some of the data types have higher-order, and some have lower order.
While performing any operations on variables with different data types in Python, 
one of the variable's data types will be changed to the higher data type. 
According to the level, one data type is converted into other by the Python interpreter itself (automatically).
This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

Example of implicit type casting:'''
# Python automatically converts
# # a to int
a = 7
print(type(a))
 
# # Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
# print(type(c))
# Ouput:
# <class 'int'>
# <class 'float'>
# 10.0
# <class 'float'>
a = 2.3;
b = 3
print(int(a)+float(b));


'''
It means in implicit type casting the variable is automatically typecasted from lower to higher order priorities . 
it indicate lower data loss . 

On thte other hand in the explicit typecasting we have to do manually typecasting
using python predefined funtions  like int()  ,str() etc .

'''