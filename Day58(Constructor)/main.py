'''

constructor ek object ko bnane me madad karta hai
constructor hamesha none return karta hai . 

'''

# class Person:
#     name="Harry";
#     occupation="Developer";
#     def info(self):
#         print(f"{self.name} is a {self.occupation}");
# a = Person();
# a.name="Divya"
# a.info()

# ab concept aata hai constructor ka 
#  jab bhi object bnayenge to constructor automaticaly ban jayega

# class Python:
#     def __init__(self , name , age):
#         print("hello");
#         self.name = name;
#         self.age = age;
#     def info(self):
#         print(f"{self.name} is a {self.age}")
# b = Python("a" , 19)
# b.info();
# c = Python()




# =============== normal code ====================
class Person:
    def details(self , name , age):
        self.name = name;
        self.age=age;
        
    def info(self):
       print(f"{self.name} is {self.age} year old");
a  = Person();
a.details("prabhat" , 12)
a.info()


# yaha pe mujhe details method ko manually call karna pada 
# lekin jab ham constructor ka use karenge tab vo automaticaly call ho jayega.
class Person1():
    def __init__(self , name , age):
        self.name = name;
        self.age  = age;
    def info1(self):
        print(f"{self.name} is {self.age} year old")
        
a1 = Person1("prabht" , 19);
a1.info1();
# matlb constructor ka use karne se only extra method calling se bacha jata hai 