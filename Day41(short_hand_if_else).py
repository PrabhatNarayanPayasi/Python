a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a>b else 0
print(c)








'''

If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the
code blocks to be executed are short. Here's an example:

a = 2
b = 330
print("A") if a > b else print("B")
You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
Another Example
result = value_if_true if condition else value_if_false
This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false
Conclusion
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.

'''

# a = 2;
# b = 18;
# print("A is smaller") if a<b else print("Not smaller") 

'''
Short-hand if-else statements ko hum ternary operator kehte hain. Ye ek tarika hai jisme aap if-else ka code ek hi line mein likhte hain.

Iska syntax kuch aise hota hai:

python
Copy
result = value_if_true if condition else value_if_false
Yahaan pe, agar condition True hai, toh value_if_true assign hota hai, aur agar False hai, toh value_if_false assign hota hai.

Example:
Maan lo tumhe ek number check karna hai ki wo even hai ya odd. Tum iss tarah se likh sakte ho:

python
Copy
number = 5
result = "Even" if number % 2 == 0 else "Odd"
print(result)
Is example mein:

Agar number even hai (matlab number % 2 == 0), toh "Even" print hoga.
Agar number odd hai, toh "Odd" print hoga.
Yeh ek short and easy way hai if-else ko likhne ka!
'''

a = 33
b = 330
print("A") if a > b else print("barabar hai bhai") if a == b else print("A chhota hai bhai")