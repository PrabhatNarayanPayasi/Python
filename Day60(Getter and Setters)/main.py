# # Python me getter aur setter methods ka use
# # object-oriented programming (OOP) me hota hai,
# # jisme aap class ke private attributes ko 
# # access (getter) ya modify (setter) karne ke 
# # liye functions define karte hain.

# # Getter:
# # Getter method ka use class ke private attributes ko read ya
# # access karne ke liye kiya jata hai.
# # Python me getter ka main purpose kisi attribute ki value ko
# # safely return karna hota hai.

# # Setter:
# # Setter method ka use class ke private attributes ko modify karne 
# # ke liye kiya jata hai. Y
# # eh method ek specific value set karta hai,
# # aur aapke class attributes ko control karne ke liye validation
# # ya logic apply kar sakte hain.

# # Example:
 
# # class Person:  
# #     def __init__(self, name, age):
# #         self.__name = name  # private attribute
# #         self.__age = age    # private attribute

# #     # Getter for name
# #     def get_name(self):
# #         return self.__name

# #     # Setter for name
# #     def set_name(self, name):
# #         self.__name = name

# #     # Getter for age
# #     def get_age(self):
# #         return self.__age

# #     # Setter for age
# #     def set_age(self, age):
# #         if age > 0:
# #             self.__age = age
# #         else:
# #             print("Age should be positive.")

# # # Object creation
# # person = Person("John", 25)

# # # Using getters
# # print(person.get_name())  # Output: John
# # print(person.get_age())   # Output: 25

# # # Using setters
# # person.set_name("Alice")
# # person.set_age(30)

# # # After modification
# # print(person.get_name())  # Output: Alice
# # print(person.get_age())   # Output: 30

# # # Invalid age setting
# # person.set_age(-5)        # Output: Age should be positive.




# # Python me property ke saath Getters aur Setters ka use:
# # Python me @property decorator ka use karke getter aur setter 
# # ko bahut clean aur easy banaya ja sakta hai. 
# # Isse aapko functions ke through attributes ko access karne 
# # ki zarurat nahi padti.

# # Example using @property:
 
# # class Person:
# #     def __init__(self, name, age):
# #         self.__name = name
# #         self.__age = age

# #     # Getter using @property
# #     @property
# #     def name(self):
# #         return self.__name

# #     # Setter using @name.setter
# #     @name.setter
# #     def name(self, value):
# #         self.__name = value

# #     # Getter for age
# #     @property
# #     def age(self):
# #         return self.__age

# #     # Setter for age with validation
# #     @age.setter
# #     def age(self, value):
# #         if value > 0:
# #             self.__age = value
# #         else:
# #             print("Age should be positive.")

# # # Object creation
# # person = Person("John", 25)

# # # Using getter
# # print(person.name)  # Output: John
# # print(person.age)   # Output: 25

# # # Using setter
# # person.name = "Alice"
# # person.age = 30

# # # After modification
# # print(person.name)  # Output: Alice
# # print(person.age)   # Output: 30

# # # Invalid age setting
# # person.age = -5      # Output: Age should be positive.
# # Key Points:




# # Getters: Private variables ko read karne ke liye.
# # Setters: Private variables ko modify karne ke liye.
# # Encapsulation: Getters aur setters ka use data ko encapsulate karne ke liye kiya jata hai, jisme aap variable ko directly access nahi karte, balki function ke through access karte hain.
# # @property decorator: 
# # Isse aap directly attribute jaise use kar sakte hain, bina get ya set methods ke call kiye.
# # Advantages of Getters and Setters:
# # Encapsulation: Internal data ko control karne ka ek tarika.
# # Validation: Setters me validation ya conditions apply karke values ko control kiya ja sakta hai.
# # Flexibility: Agar aapko future me logic change karni ho toh getter aur setter ko modify kar sakte hain bina code ke baaki parts ko affect kiye.




# class Name:
#     def __init__(self , name , age):
#         self.__name = name;
#         self.__age = age;
#     def get_name(self):
#         return self.__name;
#     def set_name(self , name):
#         self.__name = name;
        
# p = Name("Prabhat" , 13);
# print(p.get_name());

# '''

# Getter aur Setter methods aapko better encapsulation, data validation, access control, aur future flexibility deti hain.
# Aap normal functions se bhi validation kar sakte hain, lekin getter/setter methods se aap apne code ko structured aur modular bana sakte hain.
# Yeh object-oriented principles ko better implement karne mein madad karte hain, jaise encapsulation aur data hiding.

# '''
# class S:
#     def __init__(self , age):
#         self.__age = age;
#     def show(self):
#         print(self.__age)
# s = S(12);
# print(s.show())


# class M:
#     def __init__(self , age):
#         self.__age = age;
#     def get_age(self):
#         return self.__age;
# m =M(20)
# print(m.get_age())




# # isme @property aur @propertyname.setter ka use karke bhi getter and setter ka use kar skte hai
# # @ property getter aur @propertyname.setter ka use set karne ke liye kiya jata hai kisi cheej ko


class Person:
    def __init__(self , name):
        self._name1 = name;
    @property
    def name1(self):
        return self._name1;
    @name1.setter
    def mod(self , name3):
        self._name1 = name3;
person = Person("HELLO");
person._name1 = "ok";
print(person.name1)
# print(person.name1)