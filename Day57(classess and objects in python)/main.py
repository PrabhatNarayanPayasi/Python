# self matlb vo object jis par ye method call ho rha hai
# class Person:
#     name="Prabhat";
#     age:19;
#     occupation="Deve."
#     def info(self):
#         print(f"name is {self.name} age is {self.age}")
# a = Person();
# a.info();


class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person() #object matlb hai ki jab ham classes ka use karke object bnate hai to vo ek object hai jaise isme a ek object hai
# b = Person()
# c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
# b.info()
# c.info()


class Prabhat:
  print("this is prabhat");
  name="NAME"
a = Prabhat();
print(a.name)



'''

Class kya hai?
Class ek blueprint hota hai jo define karta hai ki objects kis tareeke se behave karenge. 
Isme variables (attributes) aur methods (functions) hote hain jo object ke behavior aur properties
ko define karte hain.

 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Dog class ka object bana rahe hain
dog1 = Dog("Tommy", 3)
dog1.bark()  # Tommy is barking!
Yahan Dog ek class hai. __init__() ek special method hai jise constructor kehte hain,
aur yeh class ka object banate waqt automatic call hota hai.

2. Object kya hai?
Object class ka ek instance hota hai. Jab hum class ko use karke koi variable banate hain, wo ek object hota hai. Object ke paas class ke saare attributes aur methods hoti hain.

Example me dog1 ek object hai jo Dog class ka instance hai.

3. Self keyword kya hai?
self ek special parameter hai jo har method ke first argument me hota hai. Jab hum class ka object banate hain, to self automatically us object ko refer karta hai. Matlab, jab bhi class ke andar method ko call karte hain, self us object ko refer karta hai jise method call kiya gaya.

 
class Dog:
    def __init__(self, name, age):
        self.name = name   # 'self.name' ka matlab hai object ka name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")  # self.name se hum object ka name access kar rahe hain

dog1 = Dog("Tommy", 3)
dog1.bark()  # Tommy is barking!
Yahan, jab hum dog1.bark() call karte hain, to self dog1 object ko refer karta hai. self.name ko dog1.name ke roop me samajh lo.

Summary:
Class ek template hai jo objects ko define karta hai.
Object ek instance hota hai class ka.
Self ek reference hai jo current object ko method ke through access karta hai.



'''