marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
    
    
    
    
'''
Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. 
Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
The output of this code will be:

0 apple
1 banana
2 mango
As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
This will output:

1 apple
2 banana
3 mango
The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
This will output:

1: apple
2: banana
3: mango
In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
And here's an example with a string:

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
'''

# lists = [1,2,3,4,5,6,7,8,9,10];
# for index, list in enumerate(lists):
#     print(f"Index is : {index}  , value is {list}")
# string = "Hello";
# for index , character in enumerate(string):
#     print(index+1, character)

'''
Python mein enumerate() function ka use hum kisi bhi iterable (jaise list, tuple, ya string) ke elements ke saath unka index (position) bhi lena chahte hain.

Matlab, jab hum list ke items ko iterate karte hain, toh enumerate() function humein har item ke sath uska index bhi de deta hai.

Iska syntax kuch is tarah hota hai:

python
Copy
enumerate(iterable, start=0)
Yahaan:

iterable wo list ya sequence hota hai jisko tum iterate karna chahte ho.
start (optional) tumhara index start karne ka point hota hai (default value 0 hoti hai).
Example:
Maan lo tumhare paas ek list hai:

python
Copy
fruits = ['apple', 'banana', 'cherry']
Agar tumhe har fruit ke saath uska index bhi chahiye, toh enumerate() ka use kuch is tarah karoge:

python
Copy
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
Is code mein:

index tumhe har item ka index (position) dega.
fruit tumhe har item ka value dega.
Output:

yaml
Copy
Index 0: apple
Index 1: banana
Index 2: cherry
Summary: enumerate() ka use hum isliye karte hain taaki hum item ke saath uska index bhi easily paa sakein, bina alag se index track kiye.




'''

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=4):
    print(index, fruit)