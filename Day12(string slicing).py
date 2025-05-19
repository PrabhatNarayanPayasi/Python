
'''
String Slicing & Operations on String
Length of a String
We can find the length of a string using len() function.

Example:
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
Output:
Mango is a 5 letter word.

String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
Output:
Apple
i
Note: This method of specifying the start and end index to specify a part of a string is called slicing.

Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
Output:
Apple
Pie
pleP
ApplePie




Loop through a String:
Strings are arrays and arrays are iterable.
Thus we can loop through strings.

Example:

alphabets = "ABCDE"
for i in alphabets:
    print(i)
Output:
A
B
C
D
E
'''
# name = "Prabhat"
# print(len(name))
# print(name[:2])
# print(name[3:])
# print(name[3:5])
# print(name[1:4])
# print(name[4:7])

# ye print karta h [nth index vala , n-1 index tak]
#  the slicing is done through [element at nth index , (n-1)th index ]
# print(name[3:7]);

'''fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)'''
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
# print(fruit[-1:len(fruit) - 3])
fruit = "Mango"
print(fruit[-3:-1])

# Quick Quiz:
'''nm = "rahul"
print(nm[-4:-2])
 
'''


print("Hello World");
print("Hello \" Prabhat Narayan \"");
print("\n sab badhiya");
for i in range(10):
    print(i);
string = "Narayan";
print(len(string));
# print(string[:7])
# print(string[1:7])
# print(string[2:6])
# print(string[3:4])
# print(string[4:6])
print(string[5:4]) # here the output will be empty string because whenever the starting index is higher than or equals to the end index
#  the output is empty in that case . 

# print(string[-7:])
print(string[-3:5]) # it will give y only 